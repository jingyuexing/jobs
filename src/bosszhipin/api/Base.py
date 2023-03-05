from pydantic import BaseModel
class Base(BaseModel):
    serialVersionUID = 1
    exposureAction:str