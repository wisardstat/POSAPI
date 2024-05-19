from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean
from ..database import Base

class TbProductUnit(Base):
    __tablename__ = 'tbProduct_unit'
    __table_args__ = {"schema": "dbo"}
    
    bar_code = Column(String(50))  
    pd_id = Column(String(50), nullable=False)
    seq = Column(Integer, primary_key=True)    
    unit_id = Column(Integer)
    ratio = Column(Integer)
    price1 = Column(Float)
    price2 = Column(Float)
    price3 = Column(Float)
    last_cost = Column(Float)
    cc_id = Column(String(20))
    flag_cancel = Column(String(1))
    print_barcode = Column(String(1))