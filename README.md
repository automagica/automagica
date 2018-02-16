# Automagica Client
Automagica is an open source Smart Robotic Process Automation (SRPA) platform. With Automagica, automating cross-platform processes becomes a breeze. With this open source library we want to provide a comprehensive and consistent wrapper around known and lesser known automation libraries.

![](https://github.com/OakwoodAI/automagica/blob/master/images/automagica_drawing.gif)

Refer to our website for more information: https://automagica.be

## Getting started

### Prerequisites
1. Python 3.6.4 from https://www.python.org
2. Automagica Robot ID - get one from https://automagica.be

### Installation instructions
Install Automagica on the robot host machine:
```
pip install https://github.com/OakwoodAI/automagica/tarball/master
```
## Running the Robot
1. Get your Automagica Robot ID from https://automagica.be
2. In command line or terminal run following command. Replace `<robot_id>` with your Robot ID.
```
automagica <robot_id>
```
If you do not provide a Robot ID, the application will ask for it.

### Failsafe

As a safety feature, a failsafe mechanism is enabled by default. You can trigger this by moving your mouse to the upper left corner of the screen. The failsafe is active by default. You can disable this by running the following command in the editor:
```
Failsafe(False)
```

## Credits
Under the hood, Automagica is built on some of the greatest open source libraries. Within Automagica, the following libraries are currently included:
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [socketIO-client](https://pypi.python.org/pypi/socketIO-client)

A special thanks goes out to all the above-mentioned repository contributers! :heart: