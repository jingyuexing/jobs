class SobotBaseUrl:
    api_host:str = ""
    baseHost = "https://api.sobot.com/"
    defaultHostname = "api.sobot.com/"
    @staticmethod
    def getBaseIp():
        return str(SobotBaseUrl.getApiHost()) + "chat-sdk/sdk/user/v2"
    @staticmethod
    def getApiHost():
        return SobotBaseUrl.api_host != "" if SobotBaseUrl.api_host else SobotBaseUrl.baseHost