from bosszhipin.api.Bean import Base

class ServerButtonBean(Base.BaseBean):
    ACTION_TYPE_NORMAL_HOT_STAY = 23
    serialVersionUID = -4617415375827299860
    actionType:int
    ba:str
    text:str
    url:str