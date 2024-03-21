from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class StockItem(BaseModel):
    doc_id: str  | None = None
    bar_code: str  
    pd_id: str | None = None
    pd_name: str  | None = None
    group_id: str 
    brand_id: str  
    model_id: str 
    color: str 
    cost: float  
    qty: int  
    UEDIT: str  | None = None
    DEDIT: str  | None = None
    cc_id: str  
    status_detail: str  | None = None
    _pd_code: str  | None = None
    unit_id: str  | None = None
    lot_no: str  | None = None
    bar_code_receive: str  | None = None
    qty_receive: str  | None = None
    cost_receive: str  | None = None
    STATUS: str  | None = None
    barcode_recev_change: str | None = None
    
class supplierDetail(BaseModel):
    supply_id: str  
    supply_name: str   | None = None
    supply_addr: str  | None = None
    supply_addr1: str | None = None
    supply_addr2: str | None = None
    supply_tel: str  | None = None
    supply_postcode: str  | None = None
    supply_tax_id: str  | None = None
    user_id: str  | None = None
    user_date: str  | None = None
    user_contact: str  | None = None
    cc_id: str  

class StockInRequest(BaseModel):
    doc_id: str  | None = None
    vendor_id: str  | None = None
    wh_id: str 
    vendor_name: str  
    vendor_addr1: str  | None = None
    vendor_addr2: str  | None = None
    vendor_tel: str  | None = None
    cc_id: str  
    type_doc: str  
    DOC_STATUS: str  
    itemList:List[StockItem]
    supplierDetail:supplierDetail
    class Config:
        orm_mode = True

