from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from ..database import Base

class TbStockCard(Base):
    __tablename__ = 'TbStockCard'

    seq = Column(Integer, primary_key=True, index=True)    
    doc_id = Column(String(30), nullable=False)
    doc_date = Column(DateTime)
    type_doc = Column(String(50))
    wh_id = Column(String(20))
    bar_code = Column(String(50))
    cost = Column(Float)
    qty = Column(Integer)  
    price = Column(Float)
    date_in = Column(DateTime)
    cc_id = Column(String(20))
    lot_no = Column(Integer)
    _pd_code = Column(String(50)) 
    _pd_id = Column(String(50))
    _group_id = Column(String(20))
    _brand_id = Column(String(20))
    _model_id = Column(String(20))
    _item_name = Column(String(50))
    _color = Column(String(50))
    unit_id = Column(Integer)
    vd_cu_code = Column(String(30))
    vd_cu_name = Column(String(150))
    discount = Column(Float) 
    chk_pay = Column(String(1))
    comment = Column(Text)
    type_in_doc = Column(String(10))
    doc_ref = Column(String(30))
    claim_flag = Column(String(1))
    #product = relationship("TbProductM", foreign_keys=[pd_id]) 
