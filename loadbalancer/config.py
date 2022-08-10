import yaml


class ConfigWrapper():
    def __init__(self, path):
        with open(path) as config_file:
            self.__internal = yaml.load(config_file, Loader = yaml.FullLoader)

    def get(self, key):
        return self.__internal[key]
    
    def set(self, key, value):
        self.__internal[key] = value