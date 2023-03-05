from typing import Generic, TypeVar

T = TypeVar("T")
class Base(Generic["T"]):
    code:int
    data:T
    message:str
    success:bool
    taskId:str
    time:str
    # @JSONField(alternateNames = {"traceId", "traceid"})
    traceId:str

