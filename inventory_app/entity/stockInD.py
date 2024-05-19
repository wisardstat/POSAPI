from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from ..database import Base

class TbStockInD(Base):
    __tablename__ = 'tbStock_in_d'  
    __table_args__ = {"schema": "dbo"}
    
    seq = Column(Integer, primary_key=True, index=True)    
    doc_id = Column(String(30), ForeignKey('tbStock_in_h.doc_id'))  
    bar_code = Column(String(50), nullable=True)
    pd_id = Column(String(50), nullable=True)
    pd_name = Column(String(500), nullable=True)
    group_id = Column(String(20), nullable=True)
    brand_id = Column(String(20), nullable=True)
    model_id = Column(String(20), nullable=True)
    color = Column(String(50), nullable=True)
    cost = Column(Float, nullable=True)
    qty = Column(Integer, nullable=True)
    UEDIT = Column(String(10), nullable=True)
    DEDIT = Column(DateTime, nullable=True)
    cc_id = Column(String(20), nullable=True)
    status_detail = Column(String(20), nullable=True)
    _pd_code = Column(String(50), nullable=True)
    unit_id = Column(Integer, nullable=True)
    lot_no = Column(Integer, nullable=True)
    bar_code_receive = Column(String(50), nullable=True)
    qty_receive = Column(Float, nullable=True)
    cost_receive = Column(Float, nullable=True)
    STATUS = Column(String(1), nullable=True)
    barcode_recev_change = Column(String(40), nullable=True)
