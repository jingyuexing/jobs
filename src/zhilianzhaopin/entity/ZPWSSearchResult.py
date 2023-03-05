
from typing import List
from zhilianzhaopin.entity.Base import ZPWSBase
from zhilianzhaopin.entity.ResultData import ResultData



class ZPWSSearchResult(ZPWSBase):
    data:List["ResultData"]