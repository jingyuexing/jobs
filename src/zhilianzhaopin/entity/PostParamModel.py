from pydantic import BaseModel, dataclasses
from zhilianzhaopin.entity.Operators import Operators

@dataclasses.dataclass
class PostParamModel(BaseModel):
    companyId:str;
    customerEmail:str;
    customerPhone:str;
    extendFields:str;
    fileStr:str;
    groupId:str;
    paramsExtends:str;
    partnerId:str;
    templateId:str;
    ticketContent:str;
    ticketTitle:str;
    ticketTypeId:str;
    uid:str;
    def __str__(self) -> str:
        return "PostParamModel{uid='" + self.uid + Operators.SINGLE_QUOTE + "partnerId='" + self.partnerId + Operators.SINGLE_QUOTE + ", ticketContent='" + self.ticketContent + Operators.SINGLE_QUOTE + ", customerEmail='" + self.customerEmail + Operators.SINGLE_QUOTE + ", customerPhone='" + self.customerPhone + Operators.SINGLE_QUOTE + ", companyId='" + self.companyId + Operators.SINGLE_QUOTE + ", fileStr='" + self.fileStr + Operators.SINGLE_QUOTE + ", ticketTypeId='" + self.ticketTypeId + Operators.SINGLE_QUOTE + ", groupId='" + self.groupId + Operators.SINGLE_QUOTE + ", extendFields='" + self.extendFields + Operators.SINGLE_QUOTE + ", paramsExtends='" + self.extendFields + Operators.SINGLE_QUOTE + Operators.BLOCK_END;

