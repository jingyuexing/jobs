
from typing import List

from pydantic import BaseModel

from zhilianzhaopin.entity.Base import ZPWSBase
from zhilianzhaopin.entity.DateItem import DataItem
from zhilianzhaopin.entity.ResultData import ResultData


class MatchList(BaseModel):
    matchList:List["ResultData"]

class ZPWSOccupationalSearchResult(ZPWSBase):
    data:'MatchList'