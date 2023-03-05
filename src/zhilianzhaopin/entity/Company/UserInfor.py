from pydantic import BaseModel


class User(BaseModel):
    agentId:int
    agentName:str
    avatar:str
    cityId:int
    companyId:int
    companyName:str
    createdate:int
    email:str

        # /* renamed from: ip  reason: collision with root package name */
    ip:str
    job:str
    mobile:str
    nickName:str
    nopassmessage:str
    nopassocde:int
    phone:str
    platsource:int
    provinceId:int
    rdRootCompanyId:int
    rdorgid:int
    rootCompanyId:int
    rootCompanyName:str
    sex:int
    signupsourceid:int
    sourceid:int
    staffName:str
    staffRole:int
    userCheckStatus:str
    userId:int
    userName:str
    userStatus:int
    userType:int
    weChat:str
