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

def interpret_path(path=None, required=False, addition=None, default_filename=None, random_addition=False, replace_filename=None):
    """Helper function to interpret path. This function allows for easy interpration of pathnames in the Automagica activities.
    Allows the user to give input paths both in as a raw string with backslashes, as well as a path with forward slashes.
    """
    import pathlib

    if path:
        filepath = pathlib.Path(path)
    else:    
        if not required:
            filepath = pathlib.Path.home() 
        else:
            raise Exception("No path specified, please specify a path.")
        
    if default_filename:
        filepath = filepath.joinpath(filepath, default_filename)

    if random_addition:
        if filepath.exists():
            from uuid import uuid4
            addition = "_" + str(uuid4())[:4]

    if replace_filename:
        if filepath.is_file() or filepath.is_dir():
            base = filepath.parents[0]
            out = filepath.joinpath(base, replace_filename)
            return str(out)

    if addition:
        base = filepath.parents[0]
        filename = filepath.name
        extension = filepath.suffix
        filename_base = filename.replace(extension, '')
        if base == base.parent:
            out = filename_base + addition + extension
        else:
            out = filepath.joinpath(base, filename_base + addition + extension)
        return str(out)

    return str(filepath)

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

