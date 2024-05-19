from sqlalchemy import Column, String 
from ..database import Base

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

class UserBranch(Base):

    __tablename__ = 'Tbms_user_branch' 
    __table_args__ = {"schema": "dbo"}

    user_id = Column(String(30), primary_key=True)
    wh_id = Column(String(20), nullable=True)    
    selected = Column(String(100), nullable=True)
    warehouse = relationship("UserWareHouse", back_populates="UserBranch")
    
class UserWareHouse(Base):
    
    __tablename__ = "tbWareHouse"
    __table_args__ = {"schema": "dbo"}
    
    wh_id     = Column(String(255), primary_key=True, index=True)
    wh_name   = Column(String(255))
    wh_group  = Column(String(50))
    cc_id     = Column(String(10))
    user_wh_id    = mapped_column(ForeignKey("Tbms_user_branch.wh_id"))
    UserBranch = relationship("UserBranch", back_populates="warehouse")