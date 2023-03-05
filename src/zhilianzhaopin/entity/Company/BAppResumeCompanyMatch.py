from typing import List

from pydantic import BaseModel
from zhilianzhaopin.entity.Company.Base import Base
class DetailsBean(BaseModel):
    canVisit:bool
    epName:str


class DataContent(BaseModel):
    details:List["DetailsBean"]

class BAppResumeCompanyMatch(Base["DataContent"]):
    pass