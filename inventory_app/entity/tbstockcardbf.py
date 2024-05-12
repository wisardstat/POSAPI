from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship 
from ..database import Base
 
class stockcardBF(Base):
    
    __tablename__ = "tbStockcardBF"
    
    zyear  = Column(Integer, primary_key=True, index=True)
    wh_id  = Column(String(10))
    pd_id  = Column(String(50))
    qty    = Column(Integer, nullable=True)
    amt    = Column(Float, nullable=True)
    cc_id  = Column(String(20))


    