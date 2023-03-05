
from typing import List
from zhilianzhaopin.entity.Base import ZPWSBase
from zhilianzhaopin.entity.MajorName import MajorName

class ResumeSearchMajorNameCapiEntity(ZPWSBase):
    data:List['MajorName'] = []