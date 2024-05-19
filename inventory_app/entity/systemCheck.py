from sqlalchemy import Boolean, Column, String , DateTime , TEXT , Integer
from ..database import Base

class LOG_CHECK_DATA_ERROR(Base):
    __tablename__ = 'LOG_CHECK_DATA_ERROR'  
    __table_args__ = {"schema": "dbo"}
    
    seq        = Column(Integer, primary_key=True)
    check_type = Column(String(100), nullable=True)   
    wh_id      = Column(String(100), nullable=True)    
    check_desc = Column(String(500), nullable=True)
    comment    = Column(String(500), nullable=True)
    cc_id      = Column(String(50), nullable=True)
 