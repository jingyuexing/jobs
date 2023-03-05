from bosszhipin.api.HostConfig import (
    getAddr
)


class CONFIG:
    distanceFilter = "zpCommon/config/distanceFilter"
    
    @staticmethod
    def extractApiPath():
        pass
    @staticmethod
    def extractNapiPath():
        pass
    @staticmethod
    def extractApiName():
        pass
    @staticmethod
    def isApiInList():
        pass
    @staticmethod
    def getApiAddr():
        (
            apiType,
            name,
            apiAddr,
            apiIPV6Addr,
            webAddr,
            mqttAddr,
            mqttPort,
            mqttHttpAddr,
            mqttHttpPort
        ) = getAddr().value
        return f"https://{apiAddr}/api/"
    @staticmethod
    def getWebAddr():
        (
            apiType,
            name,
            apiAddr,
            apiIPV6Addr,
            webAddr,
            mqttAddr,
            mqttPort,
            mqttHttpAddr,
            mqttHttpPort
        ) = getAddr().value
        return webAddr
    @staticmethod
    def getAPI(api:str):
        return CONFIG.getApiAddr() + api