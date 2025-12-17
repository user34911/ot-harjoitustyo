import configparser

FILEPATH = "src/config.ini"

def set_resolution(resolution):
    config = configparser.ConfigParser()
    config["DEFAULT"] = {"Width": resolution[0],
                                "Height": resolution[1]}
    with open(FILEPATH, "w") as configfile:
        config.write(configfile)

def get_resolution():
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    width = config["DEFAULT"]["Width"]
    height = config["DEFAULT"]["Height"]
    return (int(width), int(height))

def get_user():
    config = configparser.ConfigParser()
    config.read(FILEPATH)
    return config["USER"]["User"]
