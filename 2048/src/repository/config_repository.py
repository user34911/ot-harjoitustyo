import configparser

FILEPATH = "src/config.ini"

def set_resolution(resolution):
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    config["DEFAULT"] = {"width": resolution[0],
                                "height": resolution[1]}
    with open(FILEPATH, "w") as configfile:
        config.write(configfile)

def get_resolution():
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    width = config["DEFAULT"]["width"]
    width = max(int(width), 600)
    height = config["DEFAULT"]["height"]
    height = max(int(height), 600)
    return (width, height)

def get_user():
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    return config["USER"]["user"]

def set_user(username):
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    config["USER"] = {"user": str(username)}
    with open(FILEPATH, "w") as configfile:
        config.write(configfile)
