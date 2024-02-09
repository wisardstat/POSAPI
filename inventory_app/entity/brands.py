from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
 
from ..database import Base
 
class TbBrand(Base):
    
    __tablename__ = "TbBrand"
    
    brand_id   = Column(String(255), primary_key=True, index=True)
    brand_name = Column(String(255))
    #cc_id      = Column(String(3))


    