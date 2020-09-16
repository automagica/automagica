"""Copyright 2020 Oakwood Technologies BVBA"""

import inspect
import logging
import os
import pathlib
import platform
from functools import wraps
from uuid import getnode, uuid4

import psutil
from automagica.httpclient import http_client

AUTOMAGICA_ACTIVITIES = []


def activity(func):
    """
    Wrapper for Automagica activities
    """
    global AUTOMAGICA_ACTIVITIES

    # Register the activity under the AUTOMAGICA_ACTIVITIES global
    if func not in AUTOMAGICA_ACTIVITIES:
        AUTOMAGICA_ACTIVITIES.append(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function
        """
        if func.__doc__:
            name = func.__doc__.split("\n")[0]
        else:
            name = func.__name__

        logging.info("Automagica (activity): {}".format(name))
        telemetry(func)

        try:
            return func(*args, **kwargs)

        except Exception as e:
            telemetry_exception(func, e)
            raise

    return wrapper


def interpret_path(
    path=None,
    required=False,
    addition=None,
    default_filename=None,
    random_addition=False,
    replace_filename=None,
):
    """
    Helper function to interpret path. This function allows for 
    easy interpration of pathnames in the Automagica activities.
    Allows the user to give input paths both in as a raw string 
    with backslashes, as well as a path with forward slashes.
    """

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
        filename_base = filename.replace(extension, "")

        if base == base.parent:
            out = filename_base + addition + extension
        else:
            out = filepath.joinpath(base, filename_base + addition + extension)

        return str(out)

    return str(filepath)


def telemetry(func):
    """
    Automagica Activity Telemetry

    This allows us to collect information on the usage of 
    certain Automagica functionalities in order for us to keep improving 
    the software. If you would like to disable telemetry, make sure the 
    environment variable 'AUTOMAGICA_NO_TELEMETRY' is set. That way no
    information is being shared with us.
    """
    if not os.environ.get("AUTOMAGICA_NO_TELEMETRY") and not os.environ.get(
        "AUTOMAGICA_URL"
    ):
        if func.__doc__:
            name = func.__doc__.split("\n")[0]
        else:
            name = func.__name__

        data = {
            "activity": name,  # Name of the activity
            "machine_id": getnode(),  # Unique (anonymous) identifier
            "os": {
                "name": os.name,  # Operating system name
                "platform": platform.system(),  # Platform OS
                "release": platform.release(),  # Version OS
            },
        }

        try:
            _ = http_client.post(
                "https://telemetry.automagica.com/", json=data, timeout=1
            )
        except Exception:
            logging.debug("Telemetry error")


def telemetry_exception(func, exception):
    """
    Automagica Activity Telemetry for Exceptions

    This allows us to collect information on the errors in usage of 
    certain Automagica functionalities in order for us to keep improving 
    the software. If you would like to disable telemetry, make sure the 
    environment variable 'AUTOMAGICA_NO_TELEMETRY' is set. That way no
    information is being shared with us.
    """

    error = exception.__class__.__name__

    if not os.environ.get("AUTOMAGICA_NO_TELEMETRY") and not os.environ.get(
        "AUTOMAGICA_URL"
    ):
        if func.__doc__:
            name = func.__doc__.split("\n")[0]
        else:
            name = func.__name__

        data = {
            "activity": name,  # Name of the activity
            "machine_id": getnode(),  # Unique (anonymous) identifier
            "os": {
                "name": os.name,  # Operating system name
                "platform": platform.system(),  # Platform OS
                "release": platform.release(),  # Version OS
            },
            "error": error,  # Class name of the error ("ValueError" or "ZeroDivisionError")
        }

        try:
            _ = http_client.post(
                "https://telemetry.automagica.com/errors", json=data, timeout=1
            )
        except Exception:
            logging.debug("Telemetry error")


def only_supported_for(*args):
    """
    Utility function for checking platform support

    Example usage:
    only_supported_for("Windows", "Linux")
    """

    if platform.system() not in args:
        raise NotImplementedError(
            "This activity is currently only supported for {}.".format(
                ", ".join(args)
            )
        )


def all_activities():
    """
    Utility function that returns all Automagica registered activities
    in a list of dicts
    """

    def get_keywords(f):
        """
        Get the 'keywords' attribute of an Automagica activity
        """
        lines = [
            line.strip() for line in f.__doc__.split("\n") if line.strip()
        ]

        for i, line in enumerate(lines):
            if line == "Keywords":
                return [
                    keyword.strip()
                    for keyword in lines[i + 1].split(",")
                    if keyword.strip()
                ]

        return []

    def get_name(f):
        """
        Get the name of the Automagica activity
        """
        lines = [
            line.strip() for line in f.__doc__.split("\n") if line.strip()
        ]
        return lines[0]

    def get_description(f):
        """
        Get the description of the Automagica activity
        """
        lines = [
            line.strip() for line in f.__doc__.split("\n") if line.strip()
        ]
        return lines[1]

    def get_args(f):
        """
        Get the arguments of the Automagica activitiy
        """

        signature = inspect.signature(f)
        params = signature.parameters
        args = {}

        for _, val in params.items():
            arg = {
                "default": (
                    val.default if val.default != inspect._empty else ""
                )
            }

            args[val.name] = arg

            lines = [
                line.strip() for line in f.__doc__.split("\n") if line.strip()
            ]

            for line in lines:
                if line.startswith(":parameter "):
                    name = line.split(":")[1].replace("parameter ", "")
                    description = line.split(":")[-1].strip()

                    if name == val.name:
                        arg["description"] = description

                if line.startswith(":type "):
                    name = line.split(":")[1].replace("type ", "")

                    type_ = line.split(":")[-1].strip()

                    if "optional" in type_:
                        optional = True
                    else:
                        optional = False

                    type_ = type_.split(",")[0]

                    if name == val.name:
                        arg["type"] = type_
                        arg["optional"] = optional

                if line.startswith(":options "):
                    name = line.split(":")[1].replace("options ", "")
                    options_unparsed = line[line.index(":", 2) + 2 :]
                    options = eval(options_unparsed)  # nosec

                    if name == val.name:
                        arg["options"] = options

                if line.startswith(":extension "):
                    name = line.split(":")[1].replace("extension ", "")
                    extensions_unparsed = line[line.index(":", 2) + 2 :]
                    extensions = extensions_unparsed.split()

                    if name == val.name:
                        arg["extensions"] = extensions

            if not arg.get("type"):
                if val.name.endswith("path"):
                    arg["type"] = "path"

        return args

    def get_return(f):
        """
        Get the return variable from the docstring for the Automagica activity
        """
        lines = [
            line.strip() for line in f.__doc__.split("\n") if line.strip()
        ]

        for line in lines:
            if line.startswith(":return:"):
                description = line.split(":")[-1].strip()
                return {"description": description}

    def get_icon(f):
        """
        Get the 'icon' attribute for the Automagica activity
        """
        lines = [
            line.strip() for line in f.__doc__.split("\n") if line.strip()
        ]

        for i, line in enumerate(lines):
            if line.strip() == "Icon":
                return lines[i + 1].strip()

    def get_class(f):
        """
        Get the class name for the Automagica activity
        """
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
            "icon": get_icon(f),
            "key": f.__module__ + "." + f.__qualname__,
        }

        key = f.__module__ + "." + f.__qualname__
        activities[key] = activity

    return activities


def find_automagica_processes():
    """
    Find process ids (pids) for Automagica processes
    """
    pids = []

    # Walk over all processes
    for proc in psutil.process_iter():
        try:
            line = " ".join([cmd for cmd in proc.cmdline()])
            if "python" in line.lower() and "automagica" in line.lower():
                pids.append(proc.info)

        except Exception:
            logging.exception("Could not identify process")

    return pids
