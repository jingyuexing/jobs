from sqlmodel import SQLModel
from pydantic import BaseModel
class ZPWSBase(BaseModel):
    statusCode:int
    statusDescription:str;
    taskId:str;
