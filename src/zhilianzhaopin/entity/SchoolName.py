from pydantic import BaseModel


class SchoolName(BaseModel):
    displayName:str;
    intKey:int;
    kgId:str;
    overseasSchool:bool;
    schoolName:str;
    strKey:str;
