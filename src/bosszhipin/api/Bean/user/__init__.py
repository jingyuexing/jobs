from bosszhipin.api.Bean.user.MedalInfoBean import MedalInfoBean
class UserBean():
    serialVersionUID = 5952445843524896018
    anonymous:int
    avatar:str
    canPostVideo:int
    courseId:str
    identity:int
    isCertificated:int
    isRecruit:int
    isTeaching:int
    medalInfo:"MedalInfoBean"
    nickname:str
    securityId:str
    subTitle:str
    title:str
    userId:str