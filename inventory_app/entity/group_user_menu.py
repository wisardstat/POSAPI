from sqlalchemy import Column, String , Integer , ForeignKey , Boolean
from ..database import Base


class GroupUserMenu(Base):
    __tablename__ = 'group_user_menu'
    id =  Column(Integer, primary_key=True)  
    group_user_id = Column(String(10))  
    menu_id = Column(Integer)
    sub_menu_id = Column(Integer,nullable=True) 
    #group_user_id = Column(String(10), primary_key=True)  
    #menu_id = Column(Integer, ForeignKey('menus.id'), primary_key=True)
   # sub_menu_id = Column(Integer, ForeignKey('sub_menu.id'), nullable=True) 
   