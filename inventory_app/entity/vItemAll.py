from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime,Float
from sqlalchemy.orm import relationship
import datetime
from ..database import Base

class vItemAll(Base):
    __tablename__ = 'vItemAll'

    wh_id       = Column(String(50), primary_key=True, index=True)    
    wh_name     = Column(String(100))    
    bar_code    = Column(String(50))
    
    pd_id       = Column(String(50),  nullable=False ,default=None )
    pd_name     = Column(String(100),  nullable=False ,default=None )

    group_id    = Column(String(50),  nullable=False ,default=None )
    group_name  = Column(String(100),  nullable=False ,default=None )

    brand_id    = Column(String(50),  nullable=False ,default=None )
    brand_name  = Column(String(100),  nullable=False ,default=None )
    color       = Column(String(50),  nullable=False ,default=None )

    model_id    = Column(String(50),  nullable=False ,default=None )
    model_name  = Column(String(100),  nullable=False ,default=None )
    cost        = Column(Float,  nullable=True ,default=0 )    
    qty         = Column(Integer)    
    cc_id       = Column(String(10))
