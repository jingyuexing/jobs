from pydantic import BaseModel


class DataItem(BaseModel):
    intKey:str
    itemValue:str
    serial:str;
    strKey:str;