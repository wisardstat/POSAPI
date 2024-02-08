from sqlalchemy.orm import Session
from sqlalchemy import or_ , and_
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

def getListReport(db: Session
                  ,wh_id:str = ""
                  ,categoty_id:str = ""
                  ,brand_id:str = ""
                  ,type_rp:str=""
                  ,skip: int = 0
                  ,limit: int = 100):

    print('=====================================')
    print(' getListReport ')
    print(' brand_id =',brand_id)
    print(' categoty_id =',categoty_id)
    print(' type_rp =',type_rp)
    print(' wh_id =',wh_id)

    result = ( db.query(ent.vstockcard) 
              .filter(
                        and_(
                              or_( ent.vstockcard.brand_id == brand_id ,brand_id == "",brand_id == "0" )
                            , or_( ent.vstockcard.group_id == categoty_id ,categoty_id == "",categoty_id == "0" )
                            , or_( ent.vstockcard.wh_id == wh_id ,wh_id == "",wh_id == "0" )
                            , or_( and_( ent.vstockcard.qty>0 , type_rp=="EXISTS" )
                                    , and_( ent.vstockcard.qty==0 , type_rp=="NONE"  )
                                    , and_(  type_rp==""  )
                                 )
                            )
                      )              
              .order_by(ent.vstockcard.wh_name,ent.vstockcard.group_name,ent.vstockcard.brand_name)
              .offset(skip)
              .limit(limit)
              .all()
                )

    print(' row >>',len(result))

    return result
