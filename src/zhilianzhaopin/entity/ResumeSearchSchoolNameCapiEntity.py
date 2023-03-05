from typing import List
from zhilianzhaopin.entity.Base import ZPWSBase
from zhilianzhaopin.entity.SchoolName import SchoolName


class ResumeSearchSchoolNameCapiEntity(ZPWSBase):
    data:List['SchoolName'] = []