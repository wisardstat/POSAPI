from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class tbwareHouse(Base):
    
    __tablename__ = "tbWareHouse"
    schema="dbo"
    wh_id     = Column(String(255), primary_key=True, index=True)
    wh_name   = Column(String(255))
    wh_group  = Column(String(50))
    cc_id     = Column(String(10))
     