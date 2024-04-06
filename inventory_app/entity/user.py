from sqlalchemy import Column, String 
from ..database import Base

class User(Base):

    __tablename__ = 'tbms_user' 

    user_id = Column(String(30), primary_key=True)
    user_name = Column(String(30) )
    group_user_id = Column(String(20))    
    user_login = Column(String(20))
    user_password = Column(String(20))
