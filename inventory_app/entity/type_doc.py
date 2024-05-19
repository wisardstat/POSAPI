from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
 
from ..database import Base
 
class type_doc(Base):
    
    __tablename__ = "v_type_doc"
    __table_args__ = {"schema": "dbo"}
    
    type_doc_id   = Column(String(255), primary_key=True, index=True)
    type_doc_name = Column(String(255))
    type_group = Column(String(255))
    #cc_id      = Column(String(3))


    