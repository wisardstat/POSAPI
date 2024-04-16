from sqlalchemy.orm import Session
from ..entity import v_datetime_current as et
from datetime import datetime, timedelta,date

def get_current_datetime(db: Session):
    
    result = db.query(et.v_datetime_current).all()
    
    return_date = date.today()
    return_datetime = datetime.now()

    for item in result :                
        return_date = item.get_current_date
        return_datetime = item.get_current_datetime

    # cur_date,cur_datetime = cdate.get_current_datetime(db)
    # print('>> cur_date =',cur_date)
    # print('>> cur_datetime =',cur_datetime)

    return return_date,return_datetime

 