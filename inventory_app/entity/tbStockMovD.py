from sqlalchemy import Column, Integer, String, Float,DateTime
from ..database import Base

class TbStockMovD(Base):
    __tablename__ = 'tbStock_mov_d'  
    __table_args__ = {"schema": "dbo"}
    
    
    seq = Column(Integer, primary_key=True, nullable=False)
    wh_id = Column(String(10), nullable=True)
    doc_id = Column(String(15), nullable=False)
    bar_code = Column(String(20), nullable=False)
    pd_name = Column(String(50), nullable=True)
    group_id = Column(String(10), nullable=True)
    brand_id = Column(String(10), nullable=True)
    model_id = Column(String(10), nullable=True)
    color = Column(String(50), nullable=True)
    cost = Column(Float, nullable=True)
    Qty = Column(Integer, nullable=True)
    UEDIT = Column(String(10), nullable=True)
    DEDIT = Column(DateTime, nullable=True) 
    cc_id = Column(String(20), nullable=True)