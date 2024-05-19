from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from ..database import Base

class vStockInD(Base):
    __tablename__ = 'v_StockInDetail'  
    __table_args__ = {"schema": "dbo"}

    seq = Column(Integer, primary_key=True, index=True)    
    doc_id = Column(String(30), ForeignKey('tbStock_in_h.doc_id'))  
    bar_code = Column(String(50), nullable=True)    
    pd_name = Column(String(500), nullable=True)
    group_id = Column(String(20), nullable=True)
    group_name = Column(String(50), nullable=True)
    brand_id = Column(String(20), nullable=True)
    brand_name = Column(String(50), nullable=True)
    model_id = Column(String(20), nullable=True)
    model_name = Column(String(50), nullable=True)
    color = Column(String(50), nullable=True)
    cost = Column(Float, nullable=True)
    qty = Column(Integer, nullable=True)
    UEDIT = Column(String(10), nullable=True)
    DEDIT = Column(DateTime, nullable=True)
    cc_id = Column(String(20), nullable=True)
    
