from sqlalchemy import Boolean, Column, String , DateTime , TEXT
from ..database import Base

class TbStockInH(Base):
    __tablename__ = 'tbStock_in_h'  

    doc_id = Column(String(30), primary_key=True)
    doc_date = Column(DateTime, nullable=True)
    wh_id = Column(String(10), nullable=True)
    vendor_id = Column(String(20), nullable=True)
    vendor_name = Column(String(200), nullable=True)
    vendor_addr1 = Column(String(200), nullable=True)
    vendor_addr2 = Column(String(200), nullable=True)
    vendor_tel = Column(String(100), nullable=True)
    UEDIT = Column(String(10), nullable=True)
    DEDIT = Column(DateTime, nullable=True)
    cmm = Column(TEXT, nullable=True)  
    ChkChg = Column(Boolean, nullable=True)  
    itemChg = Column(String(50), nullable=True)
    cc_id = Column(String(20), nullable=True)
    type_doc = Column(String(10), nullable=True)
    doc_ref = Column(String(20), nullable=True)
    DOC_STATUS = Column(String(1), nullable=True)
