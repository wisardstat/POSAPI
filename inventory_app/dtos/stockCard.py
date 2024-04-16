from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime, timedelta,date

class StockCardItem(BaseModel):
    doc_id: str  | None = None
    doc_date : date | None = None
    type_doc : str | None = None
    wh_id: str | None = None
    bar_code: str | None = None
    cost: float  | None = None 
    qty: int  | None = None 
    price: float  | None = None 
    date_in : datetime | None = None
    cc_id: str  
    lot_no: str | None = None
    unit_id: str | None = None

    vd_cu_code: str | None = None
    vd_cu_name: str | None = None
    chk_pay: str | None = None
    comment: str | None = None
     
     