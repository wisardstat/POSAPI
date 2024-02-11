from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime,Float
from sqlalchemy.orm import relationship
import datetime
from ..database import Base


class v_stockDaily(Base):
    
    __tablename__ = "v_stockDaily"
    schema="dbo"
    seq         = Column(Integer, primary_key=True, index=True)    
    cc_id       = Column(String(10))
    
    stock_date  = Column(DateTime,default=datetime.datetime.utcnow)            
    
    wh_id       = Column(String(50))    
    wh_name     = Column(String(100))    
    bar_code    = Column(String(50))

    group_id    = Column(String(50),  nullable=False ,default=None )
    group_name  = Column(String(100),  nullable=False ,default=None )

    brand_id    = Column(String(50),  nullable=False ,default=None )
    brand_name  = Column(String(100),  nullable=False ,default=None )

    model_id    = Column(String(50),  nullable=False ,default=None )
    model_name  = Column(String(100),  nullable=False ,default=None )
    
    pd_id       = Column(String(50),  nullable=False ,default=None )
    pd_name     = Column(String(100),  nullable=False ,default=None )
    color       = Column(String(50),  nullable=False ,default=None )

    cost        = Column(Float,  nullable=True ,default=0 )    
    qty        = Column(Integer)    
    qty_zero        = Column(Integer) 
    
    
    
