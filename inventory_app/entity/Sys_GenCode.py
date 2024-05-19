from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
 
from ..database import Base
 
class Sys_GenCode(Base):
    
    __tablename__ = "IDRandom"
    __table_args__ = {"schema": "dbo"}
    
    # CrtID,Frm,TypeDoc,IDNum,cc_id

    seq     = Column(String(255), primary_key=True, index=True)
    CrtID   = Column(String(100))
    Frm     = Column(String(50))
    TypeDoc = Column(String(10))
    IDNum   = Column(Integer)
    cc_id   = Column(String(20))


    