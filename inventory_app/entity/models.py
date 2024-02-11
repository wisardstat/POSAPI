from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship 
from ..database import Base
 
class TbModel(Base):
    
    __tablename__ = "v_model"
    
    model_id   = Column(String(255), primary_key=True, index=True)
    model_name = Column(String(255))
    cc_id      = Column(String(10))


    