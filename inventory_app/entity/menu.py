from sqlalchemy import Column, String , Integer
from ..database import Base
from sqlalchemy.orm import relationship

class Menu(Base):
    __tablename__ = 'menus'
    
    id = Column(Integer, primary_key=True)
    menu_name = Column(String(255), nullable=False)
    #sub_menus = relationship('SubMenu', backref='menus')