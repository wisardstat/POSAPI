from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime, timedelta,date


class ItemDetail(BaseModel):
    doc_id: Optional[str] = None
    bar_code: str
    group_name: str
    pd_name: Optional[str] = None
    brand_name: Optional[str] = None
    cost: Optional[float] = None
    price: Optional[float] = None
    qty: Optional[int] = None
    qty_limit: Optional[int] = None
    UEDIT: Optional[str] = None
    DEDIT: Optional[str] = None
    pay_type: Optional[str] = None
    cc_id: str
    disable: bool
    group_emei: str
    wh_id: str
    wh_name: str
    pd_id: str
    group_id: str
    brand_id: str
    color: str
    model_id: str
    model_name: str
    price1: float
    price2: Optional[float] = None
    price3: Optional[float] = None
    STATUS: Optional[str] = None
    
class StockMoveRequest(BaseModel):
    doc_id: str  | None = None
    vendor_id: str  | None = None
    wh_id: str 
    vendor_name: Optional[str] = None
    wh_target: str  
    wh_from: str  
    comment: Optional[str] = None
    cc_id: str  
    type_doc: str  
    doc_date: str  
    UEDIT: str  | None = None
    DEDIT: str  | None = None
    itemList:List[ItemDetail]
    class Config:
        orm_mode = True