from bosszhipin.entity.PostParamModel import PostParamModel
from bosszhipin.entity.SobotBaseUrl import SobotBaseUrl
from bosszhipin.entity.ZhiChiUrlApi import ZhichiUrlApi
from utils.request import request


def API_ROOT(path:str):
    return f"{SobotBaseUrl.getBaseIp()}/{path}"

class Chat:
    def postMsg(self,params:PostParamModel):
        requestParams = params.dict()
        return request(API_ROOT(ZhichiUrlApi.api_post_msg),params=requestParams)
    def satisfactionMessage(self):
        pass
    def sendCardMsg():
        return request(API_ROOT(ZhichiUrlApi.api_sendFile_to_customeService))
    def sendFile():
        pass
    def sendLocation():
        pass
    def sendMsgToCoutom():
        pass
    def sendOrderCardMsg():
        pass
    def sendVoiceToRobot():
        pass
    def sobotInit():
        pass