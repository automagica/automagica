def add_credential(username=None, password=None, system='Automagica'):
    """Add a credential which stores credentials locally. All parameters should be Unicode text. 

    :param username: Username for which credential will be added.
    :param password: Password to add
    :param system: Name of the system for which credentials are stored. Extra safety measure and method for keeping passwords for similar usernames on different applications a part. Highly recommended to change default value.
    """
    import keyring
    keyring.set_password(system, username, password)

def delete_credential(username=None, password=None, system='Automagica'):
    """Delete a locally stored credential. All parameters should be Unicode text. 

    :param username: Username for which credential (username + password) will be deleted.
    :param system: Name of the system for which password will be deleted. 
    """
    import keyring
    keyring.delete_password(system, username)

def get_credential(username=None, system='Automagica'):
    """Get a saved credential. All parameters should be Unicode text. 

    :param username: Username to get password for.
    :param system: Name of the system for which credentials are retreived.
    """
    import keyring
    return keyring.get_password(system, username)

def request_password(title='Password request', dialogue_text='Enter your password:'):
    """Prompt a popup which asks user for a password and returns in plain text.
    Password will be masked on screen.
    """
    import PySimpleGUI as sg      
    sg.ChangeLookAndFeel('Reddit')      

    layout = [[sg.Text(dialogue_text)],      
                    [sg.InputText(password_char='*')],      
                    [sg.Submit(), sg.Cancel()]]      

    window = sg.Window(title, layout, icon='automagica_icon.ico')    

    event, values = window.Read()    
    window.Close()

    password_input = values[0]    
    return password_input

def request_username(title='Username request', dialogue_text='Enter your username:'):
    """Prompt a popup which asks user for a password and returns in plain text. 
    Username will not be masked.

    :param title: Title for the popup
    :param dialogue_text: Dialogue text for username
    """
    import PySimpleGUI as sg   

    sg.ChangeLookAndFeel('Reddit')      
    layout = [[sg.Text(dialogue_text)],      
                    [sg.InputText()],      
                    [sg.Submit(), sg.Cancel()]]      

    window = sg.Window(title, layout, icon='automagica_icon.ico')    
    event, values = window.Read()    
    window.Close()
    username_input = values[0]    

    return username_input

def request_credentials(title='Credential request', dialogue_text_username='Enter your username:', dialogue_text_password='Enter your username:'):
    """Prompt a popup which asks user for username and password and returns in plain text. 
    Password will be masked.

    :param title: Title for the popup
    :param dialogue_text: Dialogue text for username
    :param dialogue_text: Dialogue text for password
    """
    import PySimpleGUI as sg   

    sg.ChangeLookAndFeel('Reddit')      
    layout = [[sg.Text(dialogue_text_username)],      
                    [sg.InputText()],
                    [sg.Text(dialogue_text_password)],
                    [sg.InputText(password_char='*')],
    
                    [sg.Submit(), sg.Cancel()]]      

    window = sg.Window(title, layout, icon='automagica_icon.ico')    
    event, values = window.Read()    
    window.Close()
    username_input = values[0]
    password_input = values[1]    

    return username_input, password_input


