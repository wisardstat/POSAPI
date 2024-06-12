from sqlalchemy import Column, String , Integer
from ..database import Base
from sqlalchemy.orm import relationship

class Menu(Base):
    __tablename__ = 'tbms_menus'
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, primary_key=True)
    menu_name = Column(String(255), nullable=False)
    #sub_menus = relationship('SubMenu', backref='menus')