import configparser

config = configparser.RawConfigParser()
config.read(".//Configuration//config.ini")

class ReadConfig:
    @staticmethod
    def geturl():
        url = config.get("common information","BaseUrl")
        return url

    @staticmethod
    def getusername():
        username = config.get("common information","username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common information","password")
        return password