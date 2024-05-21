from sqlalchemy import Column, String , Integer , ForeignKey , Boolean
from ..database import Base

class SubMenu(Base):
    __tablename__ = 'sub_menu'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    icon = Column(String(50))
    type = Column(String(10), nullable=False, default='link') 
    path = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('menus.id'))
    bookmark = Column(Boolean, default=False)