from sqlalchemy import Boolean, Column, String , DateTime , TEXT
from ..database import Base

class TbCustomer(Base):
    __tablename__ = 'TbCustomer'  
    __table_args__ = {"schema": "dbo"}
    
    cust_id = Column(String(30), primary_key=True)    
    cust_title = Column(String(50), nullable=True)    
    cust_fname = Column(String(200), nullable=True)
    cust_sname = Column(String(200), nullable=True)
    cust_adr1 = Column(String(500), nullable=True)
    cust_adr2 = Column(String(500), nullable=True)
    cust_tel = Column(String(100), nullable=True)
    tax_id = Column(String(100), nullable=True)
    cc_id = Column(String(20), nullable=True)
    UEDIT = Column(String(20), nullable=True)
    DEDIT = Column(DateTime, nullable=True)
    
