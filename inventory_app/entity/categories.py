from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class tbcategory(Base):
    
    __tablename__ = "TbGroup_item"
    __table_args__ = {"schema": "dbo"}
    
    schema="dbo"
    group_id   = Column(String(255), primary_key=True, index=True)
    group_name = Column(String(255))
    group_sup  = Column(String(255))
    group_type = Column(String(255))
    group_emei = Column(String(1))
    cc_id      = Column(String(3))
    