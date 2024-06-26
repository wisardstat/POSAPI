from sqlalchemy import Column, String 
from ..database import Base
import configparser
 

class User(Base):
    __tablename__ = 'v_User' 
    __table_args__ = {"schema": "dbo"}

    user_id = Column(String(30), primary_key=True)
    user_name = Column(String(50), nullable=True)
    group_user_id = Column(String(20), nullable=True)
    group_user_name = Column(String(50), nullable=True)
    user_login = Column(String(20), nullable=True)
    user_password = Column(String(20), nullable=True)
    cc_id = Column(String(20), nullable=True)
