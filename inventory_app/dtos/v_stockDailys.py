from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta,date

class v_stockDailys_all(BaseModel):
    stock_date: date | None = None    
    wh_id: str
    wh_name: str
    bar_code: str
    group_id: str | None = None
    group_name: str | None = None
    brand_id: str | None = None
    brand_name: str | None = None
    model_id: str | None = None
    model_name: str | None = None
    pd_name: str | None = None
    color: str | None = None
    qty: int | None = None
    cost: float | None = None    
    cc_id: str  # float
    seq: int    
    class Config:
        orm_mode = True


class v_stockDailyGroupByBrand(BaseModel):
    cc_id: str  # float
    stock_date: date | None = None    
    wh_id: str
    wh_name: str        
    group_name: str | None = None    
    brand_name: str | None = None    
    qty: int | None = None

    class Config:
        orm_mode = True        


class v_stockDailyGroupByModel(BaseModel):
    cc_id: str  # float
    stock_date: date | None = None    
    wh_id: str
    wh_name: str        
    group_name: str | None = None    
    brand_name: str | None = None    
    model_name: str | None = None    
    qty: int | None = None
    
    class Config:
        orm_mode = True        
