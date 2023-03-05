from typing import List
from zhilianzhaopin.entity.Base import ZPWSBase
from zhilianzhaopin.entity.CompanyName import CompanyName


class ResumeSearchCompanyNameCapi(ZPWSBase):
    data:List["CompanyName"] = []