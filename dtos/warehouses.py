from typing import List, Optional
from pydantic import BaseModel


class warehouse(BaseModel):
    wh_id: str
    wh_name: str
    wh_group: str
    cc_id: str

    class Config:
        orm_mode = True

class warehouseCreate(warehouse):
    wh_id: str
    wh_name: str
    wh_group: str
    cc_id: str
