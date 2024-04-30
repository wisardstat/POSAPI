from sqlalchemy import Column, String ,DateTime,DATE,Float,Integer
from ..database import Base

class tbInvoiceDetail(Base):
    __tablename__ = 'TbInvoice_detail' 

    seq = Column(Integer, primary_key=True, index=True)    
    doc_id    = Column(String(30), nullable=True)    
    bar_code  = Column(String(50), nullable=True)    
    pd_name   = Column(String(500), nullable=True)    
    cost      = Column(Float, nullable=True)    
    price     = Column(Float, nullable=True)    
    qty       = Column(Integer, nullable=True)    
    unit_id   = Column(Integer, nullable=True)    

    UEDIT     = Column(String(20), nullable=True)
    DEDIT     = Column(DateTime, nullable=True)
    cc_id     = Column(String(20), nullable=True)  

    
class vInvoiceDetail(Base):
    __tablename__ = 'vInvoiceDetail' 

    seq = Column(Integer, primary_key=True, index=True)    
    doc_id    = Column(String(30), nullable=True)    
    bar_code  = Column(String(50), nullable=True)    

    pd_name    = Column(String(500), nullable=True)    
    group_name = Column(String(100), nullable=True)    
    brand_name = Column(String(100), nullable=True)    
    model_name = Column(String(100), nullable=True)    
    color      = Column(String(100), nullable=True)    

    cost      = Column(Float, nullable=True)    
    price     = Column(Float, nullable=True)    
    qty       = Column(Integer, nullable=True)  
    Amount    = Column(Float, nullable=True)      
    unit_id   = Column(Integer, nullable=True)    

    UEDIT     = Column(String(20), nullable=True)
    DEDIT     = Column(DateTime, nullable=True)
    cc_id     = Column(String(20), nullable=True)  
     
# doc_id: str | None = None
# doc_date: str | None = None
# wh_id: str | None = None
# user_id: str | None = None
# UEDIT: str | None = None
# DEDIT: str | None = None
# cc_id: str | None = None