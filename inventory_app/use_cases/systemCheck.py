from sqlalchemy.orm import Session
from sqlalchemy import  and_ ,or_ , func
from ..dtos import user as dt
from ..entity import systemCheck as ent


def get_total_problem(db: Session, wh_id:str, cc_id:str ):

    result = (
        db.query(
                   func.count(ent.LOG_CHECK_DATA_ERROR.seq).label("qty")
                 )
        .filter( and_(ent.LOG_CHECK_DATA_ERROR.wh_id == wh_id
                      ,ent.LOG_CHECK_DATA_ERROR.cc_id == cc_id )
                )        
        .all()
    )

    return result
 