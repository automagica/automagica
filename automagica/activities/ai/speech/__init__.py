def speak(text, speed=None):
    """Use the Text-To-Speech engine available on your system

    :param text: The text which should be said
    :param speed: Multiplication factor for the speed at which the text should be pronounced. 
    """
    import pyttsx3
    
    engine = pyttsx3.init()

    if speed:
        default_rate = engine.getProperty('rate')
        engine.setProperty('rate', speed * default_rate)

    engine.say(text)
    engine.runAndWait()