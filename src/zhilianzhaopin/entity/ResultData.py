from pydantic import BaseModel

from zhilianzhaopin.entity.DateItem import DataItem


class ResultData(BaseModel):
    level1:"DataItem"
    level2:"DataItem";
    level3:"DataItem";
    level4:"DataItem";