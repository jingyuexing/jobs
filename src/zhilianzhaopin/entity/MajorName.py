from pydantic import BaseModel


class MajorName(BaseModel):
    majorIntKey:int;
    majorName:str;
    majorStrKey:str;
    topIntKey:int;
    topMajorName:str;
    topStrKey:str;
