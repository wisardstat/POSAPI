from sqlalchemy import Column, String ,DateTime,Date
from ..database import Base

class v_datetime_current(Base):

    __tablename__ = 'v_datetime_current' 

    get_current_date = Column(Date, primary_key=True)
    get_current_datetime = Column(DateTime, primary_key=True)

