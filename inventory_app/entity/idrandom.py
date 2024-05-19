from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class TbIdRandom(Base):
    
    __tablename__ = 'IDRandom'
    __table_args__ = {"schema": "dbo"}

    
    CrtID = Column(String(20))
    Frm = Column(String(20))
    TypeDoc = Column(String(1))
    IDNum = Column(String(10))
    cc_id = Column(String(20))
    seq = Column(Integer, primary_key=True)
