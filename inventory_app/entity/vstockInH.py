from sqlalchemy import Boolean, Column, String , DateTime , TEXT
from ..database import Base

class vstockInH(Base):
    __tablename__ = 'v_StockInHead'  
    __table_args__ = {"schema": "dbo"}
    
    doc_id = Column(String(30), primary_key=True)
    doc_date = Column(DateTime, nullable=True)
    wh_id = Column(String(10), nullable=True)    
    wh_name = Column(String(100), nullable=True)    
    vendor_id = Column(String(20), nullable=True)
    vendor_name = Column(String(200), nullable=True)
    vendor_addr1 = Column(String(200), nullable=True)
    vendor_addr2 = Column(String(200), nullable=True)
    vendor_tel = Column(String(100), nullable=True)
    UEDIT = Column(String(10), nullable=True)
    DEDIT = Column(DateTime, nullable=True)
    cc_id = Column(String(20), nullable=True)
    DOC_STATUS = Column(String(1), nullable=True)
