from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta

class vstockcard(BaseModel):
    seq: int
    doc_id: str
    doc_date: datetime | None = None
    type_doc_id: str
    type_doc: str
    
    bar_code: str

    wh_id: str
    wh_name: str

    group_id: str | None = None
    group_name: str | None = None
    brand_id: str | None = None
    brand_name: str | None = None
    model_id: str | None = None
    model_name: str | None = None
    pd_name: str | None = None
    color: str | None = None

    cost: float | None = None
    qty: int | None = None
    qty_abs: int | None = None

    price: float | None = None
    Total: float | None = None
    
    cc_id: str  # float

    class Config:
        orm_mode = True



class vstockcard_getListByDoc(BaseModel):    
    wh_name: str
    doc_date: datetime | None = None    
    date_in: datetime | None = None        
    doc_id: str    
    type_doc: str    
    type_doc_id: str    
    cust_fname: str    
    count: int | None = None
    qty: int | None = None
    amt_cost: float | None = None
    amt_price: float | None = None
 
    class Config:
        orm_mode = True

class vstockcard_getListByDoc_Total(BaseModel):        
    count: int | None = None
    qty: int | None = None
    amt_cost: float | None = None
    amt_price: float | None = None
 
    class Config:
        orm_mode = True        