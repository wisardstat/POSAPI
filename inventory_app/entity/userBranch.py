from sqlalchemy import Column, String 
from ..database import Base

class UserBranch(Base):

    __tablename__ = 'v_UserBranch' 

    wh_id = Column(String(30), primary_key=True)
    wh_name = Column(String(100), nullable=True)
    user_id = Column(String(20), nullable=True)
    cc_id = Column(String(20), nullable=True)


    # user_id = Column(String(30), primary_key=True)
    # user_name = Column(String(50), nullable=True)
    # group_user_id = Column(String(20), nullable=True)
    # group_user_name = Column(String(50), nullable=True)
    # user_login = Column(String(20), nullable=True)    
    # status = Column(String(20), nullable=True)
