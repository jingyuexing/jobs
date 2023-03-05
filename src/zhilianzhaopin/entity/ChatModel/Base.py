from typing import Generic, TypeVar

T = TypeVar("T")
class Base(Generic["T"]):
    code:str
    data:T
    msg:str