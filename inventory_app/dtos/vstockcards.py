from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta,date

class vstockcard(BaseModel):
    seq: int
    doc_id: str
    doc_date: datetime | None = None
    date_in: datetime | None = None
    type_doc_id: str | None = None
    type_doc: str | None = None
    
    bar_code: str

    wh_id: str
    wh_name: str

    cust_id: str| None = None
    cust_fname: str| None = None

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
    cust_fname: str | None = None     
    row_key: int   
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



class vstockcard_getListByItem(BaseModel):    
    wh_name: str
    doc_date: datetime | None = None    
    date_in: datetime | None = None        
    doc_id: str    
    type_doc: str    
    type_doc_id: str    
    group_name: str    
    brand_name: str    
    model_name: str    
    pd_name: str    
    cust_fname: str    
    row_key: int   
    
    count: int | None = None
    qty: int | None = None
    qty_abs: int | None = None
    amt_cost: float | None = None
    amt_price: float | None = None
 
    class Config:
        orm_mode = True


class vstockcard_getListByItem_Total(BaseModel):    
    
    count: int | None = None
    qty: int | None = None
    qty_abs: int | None = None
    amt_cost: float | None = None
    amt_price: float | None = None
 
    class Config:
        orm_mode = True        

class BarcodeExistsRequest(BaseModel):
    bar_code: str  | None = None
    group_id: str  | None = None
    cc_id: str 



class daily_bycust(BaseModel):
    cust_id    : str  | None = None
    cust_fname : str  | None = None
    amt_price  : float  | None = None
    class Config:
        orm_mode = True     

class daily_bydate(BaseModel):
    doc_date    : date  | None = None
    qty  : int  | None = None
    qty_si  : int  | None = None
    qty_iv  : int  | None = None
    amt_cost  : float  | None = None
    amt_price  : float  | None = None
    class Config:
        orm_mode = True     


class daily_bycategory(BaseModel):    
    group_name : str  | None = None
    qty  : int  | None = None
    amt_cost  : float  | None = None
    amt_price  : float  | None = None
    class Config:
        orm_mode = True             

class daily_bybrand(BaseModel):    
    brand_name : str  | None = None
    qty  : int  | None = None
    amt_cost  : float  | None = None
    amt_price  : float  | None = None
    class Config:
        orm_mode = True                     