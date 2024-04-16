from typing import List, Optional
from pydantic import BaseModel

class vItemAll(BaseModel):
    #model_config = ConfigDict(extra='allow')
    wh_id: str   | None = None
    wh_name: str   | None = None
    bar_code: str  | None = None 
    pd_id: str  | None = None  
    pd_name: str  | None = None 
    group_id: str  | None = None 
    group_name: str  | None = None 
    brand_id: str  | None = None 
    brand_name: str  | None = None 
    color: str  | None = None 
    model_id: str  | None = None 
    model_name: str  | None = None 
    cost: float  | None = None 
    price1: float  | None = None 
    price2: float  | None = None 
    price3: float  | None = None 
    qty: int  | None = None 
    cc_id: str  | None = None 
    group_emei: str  | None = None 

    class Config:
        orm_mode = True


    # wh_id       = Column(String(50), primary_key=True, index=True)    
    # wh_name     = Column(String(100))    
    # bar_code    = Column(String(50))
    
    # pd_id       = Column(String(50),  nullable=False ,default=None )
    # pd_name     = Column(String(100),  nullable=False ,default=None )

    # group_id    = Column(String(50),  nullable=False ,default=None )
    # group_name  = Column(String(100),  nullable=False ,default=None )

    # brand_id    = Column(String(50),  nullable=False ,default=None )
    # brand_name  = Column(String(100),  nullable=False ,default=None )
    # color       = Column(String(50),  nullable=False ,default=None )

    # model_id    = Column(String(50),  nullable=False ,default=None )
    # model_name  = Column(String(100),  nullable=False ,default=None )
    # cost        = Column(Float,  nullable=True ,default=0 )    
    # qty         = Column(Integer)    
    # cc_id       = Column(String(10))
