from pydantic import BaseModel


class CapiBase(BaseModel):
    # @JSONField(alternateNames = {"code", HiAnalyticsConstant.HaKey.BI_KEY_RESULT, "StatusCode"})
    statusCode:int
    # @JSONField(alternateNames = {"message", "statusDescription", "StatusDescription"})
    statusDescription:str
    taskId:str