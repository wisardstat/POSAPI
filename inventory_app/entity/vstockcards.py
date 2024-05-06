from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime,Float
from sqlalchemy.orm import relationship
import datetime
from ..database import Base


class vstockcard(Base):
    
    __tablename__ = "v_stockCard"
    schema="dbo"
    seq         = Column(Integer, primary_key=True, index=True)
    doc_id      = Column(String(50))
    doc_date    = Column(DateTime,default=datetime.datetime.utcnow)
    date_in     = Column(DateTime,default=datetime.datetime.utcnow)
    type_doc_id = Column(String(50))
    type_doc    = Column(String(50))

    bar_code    = Column(String(50))

    wh_id       = Column(String(50))
    wh_name     = Column(String(100))    
    
    group_id    = Column(String(50),  nullable=False ,default=None )
    group_name  = Column(String(100),  nullable=False ,default=None )

    brand_id    = Column(String(50),  nullable=False ,default=None )
    brand_name  = Column(String(100),  nullable=False ,default=None )

    model_id    = Column(String(50),  nullable=False ,default=None )
    model_name  = Column(String(100),  nullable=False ,default=None )
    
    pd_name     = Column(String(100),  nullable=False ,default=None )
    color       = Column(String(50),  nullable=False ,default=None )

    cost        = Column(Float,  nullable=True ,default=0 )
    
    qty        = Column(Integer)
    qty_abs    = Column(Integer)
    qty_iv    = Column(Integer)
    qty_si    = Column(Integer)
    price      = Column(Float,  nullable=True ,default=0 )
    Total      = Column(Float,  nullable=True ,default=0 )

    cust_id     = Column(String(100),  nullable=True ,default=None )
    cust_fname  = Column(String(200),  nullable=True ,default=None )

    cc_id       = Column(String(10))
    
