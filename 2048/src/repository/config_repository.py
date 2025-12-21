import configparser

FILEPATH = "src/config.ini"

def set_resolution(resolution):
    """writes resolution to config file

    Args:
        resolution (Tuple): resolution ex. (600, 600)
    """
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    config["DEFAULT"] = {"width": resolution[0],
                                "height": resolution[1]}
    with open(FILEPATH, "w", encoding="utf-8") as configfile:
        config.write(configfile)

def get_resolution():
    """reads resolution from config file

    Returns:
        Tuple: resolution
    """
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    width = config["DEFAULT"]["width"]
    width = max(int(width), 600)
    height = config["DEFAULT"]["height"]
    height = max(int(height), 600)
    return (width, height)

def get_user():
    """reads username fron config file

    Returns:
        str: username
    """
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    return config["USER"]["user"]

def set_user(username):
    """writes username to config file

    Args:
        username (str): username to write
    """
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    config["USER"] = {"user": str(username)}
    with open(FILEPATH, "w", encoding="utf-8") as configfile:
        config.write(configfile)
