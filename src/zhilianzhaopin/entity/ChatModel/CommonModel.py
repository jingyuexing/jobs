from pydantic import BaseModel
from bosszhipin.entity.ChatModel.Base import Base
from bosszhipin.entity.ChatModel.CommonModelBase import CommonModelBase
from bosszhipin.entity.Operators import Operators
class CommonModel(Base["CommonModelBase"],BaseModel):
    serialVersionUID = 1
    msg:str
    def __str__(self) -> str:
        return "CommonModel{msg='" + self.msg + Operators.SINGLE_QUOTE + Operators.BLOCK_END;