from sqlalchemy import Column, String ,DateTime,DATE,Float
from ..database import Base

class tbInvoiceHeader(Base):

    __tablename__ = 'TbInvoice_head' 
    __table_args__ = {"schema": "dbo"}
    
    doc_id    = Column(String(30), primary_key=True)
    doc_date  = Column(DATE, nullable=True)
    wh_id     = Column(String(20), nullable=True)    

    cust_id   = Column(String(20), nullable=True)    
    cust_name   = Column(String(100), nullable=True)    
    cust_addr1   = Column(String(1000), nullable=True)    
    cust_addr2   = Column(String(1000), nullable=True)    
    cust_tel   = Column(String(50), nullable=True)    
    tax_id     = Column(String(50), nullable=True)    

    cmm = Column(String(1000), nullable=True)   # Comment / Remark 

    UEDIT     = Column(String(20), nullable=True)
    DEDIT     = Column(DateTime, nullable=True)
    cc_id     = Column(String(20), nullable=True)
    doc_type  = Column(String(20), nullable=True) # RT = Reatil (ขายปลีก) / WS = wholesale (ขายส่ง)  
    chk_pay   = Column(String(20), nullable=True) # Y = ชำระหมดแล้ว / N = ค้างชำระ
    pay_type   = Column(String(20), nullable=True) # ประเภทการชำระ : CASH (เงินสด) / TRANS (โอน)

    GrandTotal = Column(Float, nullable=True)  # Grand Total
    discount = Column(Float, nullable=True) # Discount Total
    discount_pers = Column(Float, nullable=True) 
    discount_cash = Column(Float, nullable=True)     
    TotalBeforeTax = Column(Float, nullable=True) 
    total = Column(Float, nullable=True) # Net Total

    cash_return = Column(Float, nullable=True) 
    cash_receive = Column(Float, nullable=True) 
    
    bath_txt       = Column(String(200), nullable=True) # คำอ่านค่าเเงิน ยอดรวม NetTotal
    bath_txt_vat   = Column(String(200), nullable=True) # คำอ่านค่าเเงิน ยอดรวมก่อนภาษี
    PRINT_VAT_TYPE = Column(String(20), nullable=True) # ประเภทภาษี => NO_VAT / INCLUDE_VAT (Vatนอก) /  INCLUDE_VAT (vatใน)

# doc_id: str | None = None
# doc_date: str | None = None
# wh_id: str | None = None
# user_id: str | None = None
# UEDIT: str | None = None
# DEDIT: str | None = None
# cc_id: str | None = None


class vInvoiceHeader(Base):

    __tablename__ = 'vInvoiceHead' 
    __table_args__ = {"schema": "dbo"}

    doc_id    = Column(String(30), primary_key=True)
    doc_date  = Column(DATE, nullable=True)
    wh_id     = Column(String(20), nullable=True)    
    wh_name     = Column(String(100), nullable=True)    

    cust_id   = Column(String(20), nullable=True)    
    cust_name   = Column(String(100), nullable=True)    
    cust_addr1   = Column(String(1000), nullable=True)    
    cust_addr2   = Column(String(1000), nullable=True)    
    cust_tel   = Column(String(50), nullable=True)    
    tax_id     = Column(String(50), nullable=True)    

    chk_pay     = Column(String(1), nullable=True)    

    cmm = Column(String(1000), nullable=True)   # Comment / Remark 

    UEDIT     = Column(String(20), nullable=True)
    USER_NAME     = Column(String(100), nullable=True)
    DEDIT     = Column(DateTime, nullable=True)
    cc_id     = Column(String(20), nullable=True)
    doc_type  = Column(String(20), nullable=True) # RT = Reatil (ขายปลีก) / WS = wholesale (ขายส่ง)  
    type_doc_name  = Column(String(100), nullable=True) # RT = Reatil (ขายปลีก) / WS = wholesale (ขายส่ง)  
    chk_pay   = Column(String(20), nullable=True) # Y = ชำระหมดแล้ว / N = ค้างชำระ
    pay_type   = Column(String(20), nullable=True) # ประเภทการชำระ : CASH (เงินสด) / TRANS (โอน)

    GrandTotal = Column(Float, nullable=True)  # Grand Total
    discount = Column(Float, nullable=True) # Discount Total
    discount_pers = Column(Float, nullable=True) 
    discount_cash = Column(Float, nullable=True)     
    TotalBeforeTax = Column(Float, nullable=True) 
    total = Column(Float, nullable=True) # Net Total

    tax = Column(Float, nullable=True) # Net Total
    tax_ratio = Column(Float, nullable=True) # Net Total

    cash_return = Column(Float, nullable=True) 
    cash_receive = Column(Float, nullable=True) 
    
    bath_txt       = Column(String(200), nullable=True) # คำอ่านค่าเเงิน ยอดรวม NetTotal
    bath_txt_vat   = Column(String(200), nullable=True) # คำอ่านค่าเเงิน ยอดรวมก่อนภาษี
    PRINT_VAT_TYPE = Column(String(20), nullable=True) # ประเภทภาษี => NO_VAT / INCLUDE_VAT (Vatนอก) /  INCLUDE_VAT (vatใน)
