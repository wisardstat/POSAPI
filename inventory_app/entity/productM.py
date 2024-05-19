from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean
from ..database import Base

class TbProductM(Base):
    __tablename__ = 'TbProductM'
    __table_args__ = {"schema": "dbo"}
    
    pd_id = Column(String(50), primary_key=True)
    pd_name = Column(String(200))
    group_id = Column(String(20))
    brand_id = Column(String(20))
    model_id = Column(String(20))
    color = Column(String(50))
    _bar_code = Column(String(50))  
    img_id = Column(String(200))
    _unit_small_id = Column(Integer)
    _unit_pack_id = Column(Integer)
    _unit_packing = Column(Integer)
    _unit_size = Column(String(50))
    cc_id = Column(String(50))
    pd_id_old = Column(String(50))
    cost = Column(Float)
    point_buy = Column(Integer)
    chk_cancel = Column(String(1))
    warranty_mn = Column(Integer)
    price = Column(Float)
    date_in = Column(DateTime)
    pd_id_new = Column(String(40))
    price1 = Column(Float)
    price2 = Column(Float)
    price3 = Column(Float)
    min_qty = Column(Integer)
    max_qty = Column(Integer)
    flag_show_front = Column(Boolean)