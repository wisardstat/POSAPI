from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class tbwareHouse(Base):
    
    __tablename__ = "tbWareHouse"
    schema="dbo"
    wh_id     = Column(String(255), primary_key=True, index=True)
    wh_name   = Column(String(255))
    wh_group  = Column(String(50))
    company_name  = Column(String(100))
    addr1   = Column(String(1000))
    addr2   = Column(String(1000))
    tel     = Column(String(100))
    tax_no  = Column(String(50))
    cmm_slip_bill1  = Column(String(1000))
    cmm_slip_bill2  = Column(String(1000))
    cc_id     = Column(String(10))
     