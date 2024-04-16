from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime, timedelta,date

class customer(BaseModel):
    #model_config = ConfigDict(extra='allow')
    cust_id: str | None = None
    cust_title: str | None = None
    cust_fname: str | None = None
    cust_sname: str | None = None
    cust_adr1: str | None = None
    cust_adr2: str | None = None
    cust_tel: str | None = None
    tax_id: str | None = None    
    cc_id: str | None = None
    UEDIT: str | None = None
    DEDIT: date | None = None

    class Config:
        orm_mode = True
  