from sqlalchemy import Column, String , Integer , ForeignKey , Boolean
from ..database import Base

class SubMenu(Base):
    __tablename__ = 'tbms_menu_sub'
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    icon = Column(String(50))
    type = Column(String(10), nullable=False, default='link') 
    path = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('tbms_menus.id'))
    bookmark = Column(Boolean, default=False)