from typing import List, Optional
from pydantic import BaseModel

class userBranch(BaseModel):
    #model_config = ConfigDict(extra='allow')
    wh_id: str   | None = None
    wh_name: str   | None = None
    user_id: str  | None = None 

    # user_id: str  | None = None 
    # user_name: str  | None = None     
    # group_user_id: str  | None = None     
    # group_user_name: str  | None = None     
    # user_login: str  | None = None     
    # user_password: str  | None = None     
    # wh_id: str   | None = None
    # wh_name: str   | None = None
    # cc_id: str   | None = None    
    # status: str   | None = None    

    class Config:
        orm_mode = True

