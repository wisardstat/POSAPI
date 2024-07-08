from sqlalchemy import Column, String, DateTime, Text
from ..database import Base

class TbStockMovH(Base):
    __tablename__ = 'TbStock_mov_h'  
    __table_args__ = {"schema": "dbo"}


    doc_id = Column(String(20), primary_key=True, nullable=False)
    doc_date = Column(DateTime, nullable=True)
    wh_from = Column(String(20), nullable=True)
    wh_target = Column(String(20), nullable=True)
    comment = Column(Text, nullable=True)
    UEDIT = Column(String(10), nullable=True)
    DEDIT = Column(DateTime, nullable=True)
    cc_id = Column(String(20), nullable=True)