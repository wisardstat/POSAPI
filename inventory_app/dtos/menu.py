from typing import List, Optional
from pydantic import BaseModel, Field

class SubMenu(BaseModel):
    path: str
    title: str
    type: str = "link" 
    icon: Optional[str] = None
    bookmark: bool = False

class Menu(BaseModel):
    title: str
    icon: str
    type: str = "sub"  
    active: bool = False
    children: List[SubMenu] = Field(default_factory=list)