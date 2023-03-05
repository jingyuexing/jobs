from pydantic import BaseModel
from zhilianzhaopin.entity.Company.Base import Base


class CompanyInfor(BaseModel):
    businesslicencepath:str
    businesslicenceurl:str
    businesslicenceurlname:str
    canModifyCompanyInfo:bool;
    cityid:int
    companySize:int
    companyaddress:str;
    companyid:int;
    companyname:str
    companytype:int
    contactor:str
    cqid:int
    createstaffid:int
    email:str
    fax:str
    hostid:int
    industryFilledSource:str
    industryid:str
    industryid2:str
    isShowBubble:bool
    iscompany:str
    iscomplated:bool
    latitude:str
    logourl:str
    longitude:str
    mobile:str
    modifystaffid:int
    newIndustry:str
    orgdescription:str
    orgid:int
    orgname:str
    orgnumber:str
    orgshortname:str
    parentid:int
    postalcode:str
    provinceid:int
    redirectType:int
    status:int
    telephone:str
    url:str
    zoomlevel:int
class CompanyInforItem(Base["CompanyInfor"]):
    pass
