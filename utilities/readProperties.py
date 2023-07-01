import configparser

config = configparser.RawConfigParser()
config.read(".\\Configration\\config.ini")

class RawConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get("common info", "url")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username
    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
    
    @staticmethod
    def getXlPath():
        path = config.get("common info", "xlpath")
        return path
    
    
