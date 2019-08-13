import argparse
import json
import logging
import os
import subprocess
import sys
from time import sleep

__version__ = '1.0.0'

parser = argparse.ArgumentParser(description='Automagica Robot')

parser.add_argument('--login', 
                    dest='login',
                    action='store_true', 
                    help='Log in')

parser.add_argument('--logout', 
                    dest='logout',
                    action='store_true', 
                    help='Log out')

parser.add_argument('--daemon', 
                    dest='daemon',
                    action='store_true', 
                    help='Run robot as a daemon')

parser.add_argument('--foreground', 
                    dest='foreground', 
                    default=False,
                    action='store_true', 
                    help='Keep process in the foreground')

parser.add_argument('--config', 
                    dest='config',
                    action='store_true', 
                    help='Alternate path to config')

parser.add_argument('-f', 
                    '--file', 
                    default='',
                    type=str, 
                    help='Path to script file')

parser.add_argument('-s', 
                    '--script', 
                    default='', 
                    type=str,
                    help='Script string for the Automagica robot (if no --file not specified)')

parser.add_argument('-p', 
                    '--parameters', 
                    default='', 
                    type=str,
                    help='Parameters string for the Automagica Bot')

parser.add_argument('--ignore-warnings', 
                    dest='ignore_warnings', 
                    default=False, 
                    action='store_true',
                    help='Python warnings will not end up in stderr')

parser.add_argument('--verbose', 
                    dest='verbose', 
                    default=False, 
                    action='store_true', 
                    help='Verbose logging')


class Automagica():
    def __init__(self):
        # Process arguments
        args = parser.parse_args()

        # Set up logging
        self._setup_logging(verbose=args.verbose)

        # Environment variable override Automagica Portal URL
        self.url = os.environ.get('AUTOMAGICA_URL', 'https://portal.automagica.dev')
        
        # Custom config specified?
        if args.config:
            self.config_path = args.config
        else:
            self.config_path = os.path.join(os.path.expanduser('~'), 'automagica.json')
        
        self.config = self.load_config()

        if args.login:
            self.login()

        if args.logout:
            self.logout()

        if args.daemon:
            self.daemon(foreground=args.foreground)

        # Was a file specified?
        if args.file:
            with open(args.file) as f:
                script = f.read()
        else:
            script = args.script

        # Ignore warnings
        if args.ignore_warnings:
            import warnings
            warnings.simplefilter('ignore')

        # Parameters specified
        if args.parameters:
            exec(args.parameters, globals())

        # Run script
        exec(script, globals())
            
    
    def _setup_logging(self, verbose=False):
        if verbose:
            log_level = logging.INFO
        else:
            log_level = logging.WARNING

        formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')

        logger = logging.getLogger()
        logger.setLevel(log_level)

        # Log to file
        logging_path = os.path.join(os.path.expanduser('~'), 'automagica.log')
        file_handler = logging.FileHandler(logging_path)
        file_handler.setFormatter(formatter)

        # Log to console
        stdout_handler = logging.StreamHandler(sys.stdout)

        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f)

    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)

        except FileNotFoundError:
            config = {}
            self.config = config
            self.save_config()

        return config

    def daemon(self, foreground=False):
        import socketio

        if not foreground:
            # Hide console if we're on Windows
            if os.name == 'nt':
                import ctypes
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

        sio = socketio.Client()

        if not self.config.get('bot_id'):
            raise Exception('You need to log in first!')

        @sio.on('connect', namespace='/bot')
        def connect():
            logging.info('Connected')

            # After connecting, send authentication message
            sio.emit('auth', {
                'bot_id': self.config['bot_id'],
                'version': __version__
                }, namespace='/bot')

        @sio.on('run', namespace='/bot')
        def run(data):
            logging.info('Running script')
            logging.info(str(data))

            job_id = data['schedule']['job']['id']

            # Save backup of the script
            fn = str(job_id)+'.py'
            path = os.path.join(os.getcwd(), fn) 

            with open(fn, 'w') as f:
                f.write(data['schedule']['script']['code'])
            
            cmd = sys.executable + ' -u -m automagica -f ' + path

            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE)

            @sio.on('kill', namespace='/bot')
            def kill(job):
                if job == job_id:
                    p.kill()
                    logging.info('Stopping job')

            # Read STDOUT
            for line in iter(p.stdout.readline, b''):
                if line:
                    output = {
                        'output': line.decode('utf-8') ,
                        'job_id': job_id,
                        'bot_id': self.config['bot_id']
                    }
                    sio.emit('output', output, namespace='/bot')
            
            # Read STDERR
            for line in iter(p.stderr.readline, b''):
                if line:
                    error = {
                        'error': line.decode('utf-8') ,
                        'job_id': job_id,
                        'bot_id': self.config['bot_id']
                    }
                    sio.emit('error', error, namespace='/bot')
            
            # Wait for process to finish
            p.wait()

            # Retrieve status code
            code = p.poll()  

            result = {
                'job_id': job_id,
                'bot_id': self.config['bot_id'],
            }

            if code == 0: # Success
                result['type'] = 'success'
            else: # Failure
                result['type'] = 'failure'
            
            logging.info('Finished script!')
            
            sio.emit('finish', result, namespace='/bot')

        @sio.on('disconnect', namespace='/bot')
        def disconnect():
            logging.info('Disconnected')

        @sio.on('authed', namespace='/bot')
        def authed(data):
            logging.info('Authenticated to Automagica as {}'.format(data['bot']['name']))

        @sio.on('error', namespace='/bot')
        def error(data):
            logging.info(data.get('error'))
            try:
                from tkinter import messagebox
                messagebox.showwarning('Error', data.get('error'))

                if data.get('url'):
                    import webbrowser
                    webbrowser.open(data['url'])
            except:
                logging.error(data.get('error'))


        while True:
            try:
                sio.connect(self.url)
                sio.wait()
            except:
                logging.info('Could not connect to Automagica, retrying in 5 seconds.')
                sleep(5)

    def kill_process(self, name):
        import psutil
        for proc in psutil.process_iter():
            if proc.name() == name or proc.name() == name + '.exe':
                if proc.pid != os.getpid(): # Don't kill yourself
                    proc.kill()
                    proc.wait()

    def login(self):
        import requests
        import platform
        import getpass
        
        # Clear the console
        clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
        clear()

        print('Welcome to Automagica!\n')
        print('Sign up for an account at https://portal.automagica.dev \n')

        name = platform.node()

        while True:
            print('\n')
            email = input('Please enter your e-mail: ')
            password = getpass.getpass('Please enter your password: ')
            print('\n')

            data = {
                'email': email,
                'password': password,
                'name': name,
            }

            
            r = requests.post(self.url+'/client-login', json=data)

            if r.status_code == 200:
                result = r.json()

                if result.get('error'):
                    if result.get('url'):
                        try:
                            import webbrowser
                            webbrowser.open(result['url'])
                        except:
                            print('Find more information at: ' + result['url'])

                    print(result['error'])
                
                if result.get('bot_id'):
                    self.config['bot_id'] = result['bot_id']
                    self.save_config()

                    self.add_startup()
                    self.kill_process('automagica')

                    command = 'automagica --daemon'
                    subprocess.Popen(command, close_fds=True)
                    

            else:
                print('Could not connect to Automagica at {}'.format(self.url))

    def logout(self):
        self.remove_startup()

    def add_startup(self):
        import platform

        cmd = sys.executable + ' -m automagica --daemon'

        if platform.system() == 'Windows':
            import winreg as reg         
            registry = reg.OpenKey(reg.HKEY_CURRENT_USER,
                                    'Software\Microsoft\Windows\CurrentVersion\Run',
                                    0,
                                    reg.KEY_WRITE) 
            reg.SetValueEx(registry,'Automagica', 0, reg.REG_SZ, cmd) 
            reg.CloseKey(registry) 

        if platform.system() == 'Linux':
            # Create Automagica.desktop file in ~/.config/autostart/
            path = os.path.join(os.path.expanduser('~'), '.config/autostart/Automagica.desktop')
            with open(path, 'w') as f:
                contents =  """[Desktop Entry] 
                            Type=Application
                            Exec="""+ cmd
                f.write(contents)

        if platform.system() == 'Darwin':
            # Create com.automagica.robot.plist file in ~/Library/LaunchAgents
            path = os.path.join(os.path.expanduser('~'), 'Library/LaunchAgents/com.automagica.robot.plist')
            with open(path, 'w') as f:
                contents = """<?xml version="1.0" encoding="UTF-8"?>
                            <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
                            <plist version="1.0">
                            <dict>
                            <key>Label</key>
                            <string>com.automagica.robot</string>
                            <key>ProgramArguments</key>
                            <array>
                            <string>"""+cmd+"""</string>
                            </array>
                            <key>RunAtLoad</key>
                            <true/>
                            </dict>
                            </plist>"""

    def remove_startup(self):
        import platform

        if platform.system() == 'Windows':
            import winreg as reg         
            registry = reg.OpenKey(reg.HKEY_CURRENT_USER,
                                    'Software\Microsoft\Windows\CurrentVersion\Run',
                                    0,
                                    reg.KEY_WRITE) 
            reg.DeleteValue(registry, 'Automagica')
            reg.CloseKey(registry)     

        if platform.system() == 'Linux':
            path = os.path.join(os.path.expanduser('~'), '.config/autostart/Automagica.desktop')
            os.remove(path)
            
        if platform.system() == 'Darwin':
            path = os.path.join(os.path.expanduser('~'), '/Library/LaunchAgents/com.automagica.robot.plist')
            os.remove(path)


def main():
    app = Automagica()

if __name__ == '__main__':
    main()
else:
    from .activities import *

