from enum import Enum

class HostConfig:
    mqttPort:int = 2345
    mqttHttpPort:int = 80

class Addr(Enum):
    ONLINE=(1, "线上环境", "api5.zhipin.com", "api-and.zhipin.com", "https://m.zhipin.com/", "chat.zhipin.com", HostConfig.mqttPort, "hchat.zhipin.com", HostConfig.mqttHttpPort)
    OFFLINE=(2, "线下环境", "boss-api.weizhipin.com", "https://boss-m.weizhipin.com/", None, "192.168.18.178", HostConfig.mqttPort, "192.168.18.178", HostConfig.mqttHttpPort)
    QA1=(3, "QA环境", "boss-api-qa.weizhipin.com", None, "https://boss-m-qa.weizhipin.com/", "192.168.18.70", HostConfig.mqttPort, None, HostConfig.mqttHttpPort)
    PUBLIC=(4, "外网环境", "boss-api2.weizhipin.com", None, "https://boss-m-qa2.weizhipin.com/", "boss-chat.weizhipin.com", HostConfig.mqttPort, None, HostConfig.mqttHttpPort)
    PRE=(5, "预发环境", "pre-api.bosszhipin.com", None, "https://pre-www.zhipin.com/", "47.95.203.120", HostConfig.mqttPort, "47.85.203.120", HostConfig.mqttHttpPort)
    QA2=(6, "QA2环境", "boss-api-qa2.weizhipin.com", None, "https://boss-m-qa2.weizhipin.com/", "192.168.1.155", HostConfig.mqttPort, None, HostConfig.mqttHttpPort)
    QA3=(7, "QA3环境", "boss-api-qa3.weizhipin.com", None, "https://boss-m-qa3.weizhipin.com/", "192.168.1.170", HostConfig.mqttPort, None, HostConfig.mqttHttpPort)
    QA4=(8, "QA4环境", "boss-api-qa4.weizhipin.com", None, "https://boss-m-qa4.weizhipin.com/", "192.168.1.185", HostConfig.mqttPort, None, HostConfig.mqttHttpPort)

def getAddr(apiType:int = 1):
    API = [
        Addr.ONLINE,
        Addr.OFFLINE,
        Addr.QA1,
        Addr.PUBLIC,
        Addr.PRE,
        Addr.QA2,
        Addr.QA3,
        Addr.QA4 
    ]
    if(apiType < 8):
        return API[apiType]
    else:
        return API[1]
