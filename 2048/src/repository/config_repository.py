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
    height = config["DEFAULT"]["height"]
    return (int(width), int(height))

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
