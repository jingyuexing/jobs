from pydantic import BaseModel


class BaseBean(BaseModel):
    serialVersionUID = 1
    exposureAction:str