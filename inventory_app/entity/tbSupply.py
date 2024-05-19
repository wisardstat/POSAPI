from sqlalchemy import Column, String, DateTime
from ..database import Base

class TbSupply(Base):
    __tablename__ = 'TbSupply' 
    __table_args__ = {"schema": "dbo"}
    
    supply_id = Column(String(20), primary_key=True)
    supply_name = Column(String(150), nullable=True)
    supply_addr = Column(String(250), nullable=True)    
    supply_addr1 = Column(String(250), nullable=True)
    supply_addr2 = Column(String(250), nullable=True)
    supply_tel = Column(String(100), nullable=True)
    supply_postcode = Column(String(10), nullable=True)
    supply_tax_id = Column(String(20), nullable=True)
    user_id = Column(String(10), nullable=True)
    user_date = Column(DateTime, nullable=True)
    user_contact = Column(String(50), nullable=True)
    cc_id = Column(String(20), nullable=True)
