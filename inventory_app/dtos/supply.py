from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime, timedelta,date

class supply(BaseModel):
    #model_config = ConfigDict(extra='allow')
    supply_id: str | None = None
    supply_name: str | None = None
    supply_addr: str | None = None
    supply_addr1: str | None = None
    supply_addr2: str | None = None
    supply_tel: str | None = None
    supply_postcode: str | None = None
    supply_tax_id: str | None = None
    user_id: str | None = None
    user_date: date | None = None
    user_contact: str | None = None
    cc_id: str | None = None

    class Config:
        orm_mode = True
 

 