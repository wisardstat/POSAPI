from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime, timedelta,date

class customerRequest(BaseModel):
    #model_config = ConfigDict(extra='allow')
    cust_id: str | None = None
    cust_title: str | None = None
    cust_fname: str | None = None
    cust_sname: str | None = None
    cust_addr1: str | None = None
    cust_addr2: str | None = None
    cust_tel: str | None = None
    tax_id: str | None = None    
    cc_id: str | None = None
    # UEDIT: str | None = None
    # DEDIT: date | None = None
    
  
class ItemListRequest(BaseModel):    
    bar_code: str | None = None
    group_name: str | None = None
    pd_name: str | None = None
    cost: str | None = None
    price: str | None = None
    qty: str | None = None
    qty_limit: str | None = None
    UEDIT: str | None = None
    pay_type: str | None = None
    cc_id: str | None = None
    disable: str | None = None
    group_emei: str | None = None

class SaleHeaderRequest(BaseModel):   

    doc_id: str | None = None
    doc_date: str | None = None
    wh_id: str | None = None

    user_id: str | None = None

    cust_id: str | None = None
    cust_name: str | None = None
    cust_addr1: str | None = None
    cust_addr2: str | None = None
    cust_tel: str | None = None
    tax_id: str | None = None

    cmm: str | None = None

    UEDIT: str | None = None
    
    cc_id: str | None = None
    doc_type: str | None = None
    chk_pay: str | None = None
    pay_type: str | None = None

    GrandTotal: float | None = None
    discount: float | None = None
    discount_pers: float | None = None
    discount_cash: float | None = None
    TotalBeforeTax: float | None = None
    total: float | None = None

    cash_return: float | None = None
    cash_receive: float | None = None
    
    # bath_txt: str | None = None
    # bath_txt_vat: str | None = None
    PRINT_VAT_TYPE: str | None = None

    itemList:List[ItemListRequest]
    customerDetail:customerRequest
    class Config:
        orm_mode = True

class SaleDetailRequest(BaseModel): 

    doc_id   : str | None = None
    bar_code : str | None = None
    pd_name  : str | None = None
    cost     : float | None = None
    price    : float | None = None
    qty      : int | None = None
    unit_id  : int | None = None
    UEDIT    : str | None = None
    DEDIT    : datetime | None = None
    cc_id    : str | None = None


class InvoiceHeader(BaseModel):

    doc_id    : str | None = None
    doc_date  : date | None = None
    wh_id     : str | None = None

    cust_id    : str | None = None
    cust_name  : str | None = None
    cust_addr1 : str | None = None
    cust_addr2 : str | None = None
    cust_tel   : str | None = None
    tax_id     : str | None = None

    cmm  : str | None = None

    UEDIT     : str | None = None
    DEDIT     : datetime | None = None
    cc_id     : str | None = None
    doc_type  : str | None = None
    chk_pay   : str | None = None
    pay_type  : str | None = None

    GrandTotal : float | None = None
    discount   : float | None = None
    discount_pers : float | None = None
    discount_cash : float | None = None
    TotalBeforeTax : float | None = None
    total : float | None = None

    cash_return : float | None = None
    cash_receive : float | None = None
    
    bath_txt       : str | None = None
    bath_txt_vat   : str | None = None
    PRINT_VAT_TYPE : str | None = None


class InvoiceRequest(BaseModel): 

     saleHeader: InvoiceHeader 
     # itemList:List[ItemListRequest]

# class tbInvoiceHeader(BaseModel):    
#     doc_id: str | None = None
#     doc_date: str | None = None
#     wh_id: str | None = None
#     cust_id: str | None = None
#     user_id: str | None = None
#     UEDIT: str | None = None
#     DEDIT: str | None = None
#     cc_id: str | None = None
#     doc_type: str | None = None

#     class Config:
#         orm_mode = True