from typing import List
from bosszhipin.api.Bean.Base import BaseBean

from bosszhipin.api.Bean.ServerButtonBean import ServerButtonBean


class VIPBuyDialogBean(BaseBean):
    serialVersionUID = 8723936346047929434
    buttonList:List["ServerButtonBean"]
    content:str
    title:str