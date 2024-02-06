from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..entity import vstockcards as ent


def get_vstockcard_bysingle(db: Session, wh_id: str):
    return (
              db.query(ent.vstockcard)
                .filter(ent.vstockcard.wh_id == wh_id)
                .first()
            )

def getListAll(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(ent.vstockcard)
        .order_by(ent.vstockcard.wh_name,ent.vstockcard.group_name,ent.vstockcard.brand_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

def getListReport(db: Session,brand_id:str = "",skip: int = 0, limit: int = 100):

    print('=====================================')
    print(' getListReport ')
    print(' brand_id =',brand_id)
    result = ( db.query(ent.vstockcard) 
              .filter(or_( ent.vstockcard.brand_id == brand_id ,brand_id == "",brand_id == "0" ))
              .order_by(ent.vstockcard.wh_name,ent.vstockcard.group_name,ent.vstockcard.brand_name)
              .offset(skip)
              .limit(limit)
              .all()
                )

    print(' row >>',len(result))

    return result
