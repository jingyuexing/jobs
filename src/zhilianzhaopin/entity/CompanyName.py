from pydantic import BaseModel


class CompanyName(BaseModel):
    companyName:str;
    displayName:str;
    industryCodeNew:str;
    intKey:int;
    kgId:str;
    strKey:str;
