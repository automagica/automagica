def activity(func):
    """Wrapper for Automagica activities
    """
    from functools import wraps
    import logging

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function
        """
        if func.__doc__:
            name = func.__doc__.split("\n")[0]
        else:
            name = func.__name__
        logging.info("Automagica (activity): {}".format(name))
        telemetry(func)
        return func(*args, **kwargs)

    return wrapper


def telemetry(func):
    """Automagica Activity Telemetry

    This allows us to collect information on the usage of 
    certain Automagica functionalities in order for us to keep improving 
    the software. If you would like to disable telemetry, make sure the 
    environment variable 'AUTOMAGICA_NO_TELEMETRY' is set. That way no
    information is being shared with us.
    """
    import requests
    from uuid import getnode
    import os
    import platform

    if not os.environ.get("AUTOMAGICA_NO_TELEMETRY") and not os.environ.get(
        "AUTOMAGICA_URL"
    ):
        if func.__doc__:
            name = func.__doc__.split("\n")[0]
        else:
            name = func.__name__

        data = {
            "activity": name,
            "machine_id": getnode(),
            "os": {
                "name": os.name,
                "platform": platform.system(),
                "release": platform.release(),
            },
        }

        try:
            r = requests.post("https://telemetry.automagica.com/", json=data, timeout=1)
        except:
            pass


def only_supported_for(*args):
    """Utility function for checking platform support

    Example usage:
    only_supported_for("Windows", "Linux")
    """
    import platform

    if platform.system() not in args:
        raise NotImplementedError(
            "This activity is currently only supported for {}.".format(", ".join(args))
        )

