AUTOMAGICA_ACTIVITIES = []


def activity(func):
    """Wrapper for Automagica activities
    """
    from functools import wraps
    import logging

    global AUTOMAGICA_ACTIVITIES

    if func not in AUTOMAGICA_ACTIVITIES:
        AUTOMAGICA_ACTIVITIES.append(func)

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


def all_activities():
    """Utility function that returns all Automagica registered activities
    in a list of dicts
    """

    def get_keywords(f):
        lines = [line.strip() for line in f.__doc__.split("\n") if line.strip()]

        for i, line in enumerate(lines):
            if line == "Keywords":
                return [
                    keyword.strip()
                    for keyword in lines[i + 1].split(",")
                    if keyword.strip()
                ]

        return []

    def get_name(f):
        lines = [line.strip() for line in f.__doc__.split("\n") if line.strip()]
        return lines[0]

    def get_description(f):
        lines = [line.strip() for line in f.__doc__.split("\n") if line.strip()]
        return lines[1]

    def get_args(f):
        import inspect

        signature = inspect.signature(f)
        params = signature.parameters
        args = []

        for _, val in params.items():
            arg = {
                "name": val.name,
                "default": (val.default if val.default != inspect._empty else None),
            }
            args.append(arg)

            lines = [line.strip() for line in f.__doc__.split("\n") if line.strip()]

            for line in lines:
                if line.startswith(":parameter "):
                    name = line.split(":")[1].replace("parameter ", "")
                    description = line.split(":")[-1].strip()

                    if name == val.name:
                        arg["description"] = description

                if line.startswith(":type "):
                    name = line.split(":")[1].replace("type ", "")
                    type_ = line.split(":")[-1].strip()

                    if name == val.name:
                        arg["type"] = type_

            # TODO: not all activities have types defined for all arguments
            for arg in args:
                if not arg.get("type"):
                    if arg.get("name").endswith("path"):
                        arg["type"] = "path"

        return args

    def get_return(f):
        lines = [line.strip() for line in f.__doc__.split("\n") if line.strip()]

        for line in lines:
            if line.startswith(":return:"):
                description = line.split(":")[-1].strip()
                return {"description": description}

    def get_class(f):
        name = f.__qualname__

        class_name = f.__qualname__.split(".")[0]

        if class_name != name:
            return class_name

    activities = {}

    for f in AUTOMAGICA_ACTIVITIES:
        activity = {
            "keywords": get_keywords(f),
            "name": get_name(f),
            "description": get_description(f),
            "args": get_args(f),
            "return": get_return(f),
            "class": get_class(f),
        }

        key = f.__module__ + "." + f.__qualname__
        activities[key] = activity

    return activities
