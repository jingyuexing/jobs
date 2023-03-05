from typing import Dict,Any
from httpx import get


def request(api:str="",params:Dict[str,str] = {})->Any:
    response =  get(url=api,params=params)
    if(response.status_code == 200):
        return response.json()
    else:
        return {}