from sqlalchemy.orm import Session
from sqlalchemy import or_ , and_  , func
from ..entity import v_stockDailys as ent


def getSingle(db: Session, wh_id: str):
    return (
              db.query(ent.v_stockDaily)
                .filter(ent.v_stockDaily.wh_id == wh_id)
                .first()
            )

def getListAll(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(ent.v_stockDaily)
        .order_by(ent.v_stockDaily.wh_name,ent.v_stockDaily.group_name,ent.v_stockDaily.brand_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

def getListGroupByBrand(db: Session
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

    result = ( db.query(ent.v_stockDaily.cc_id,
                        ent.v_stockDaily.stock_date,
                        ent.v_stockDaily.wh_id,
                        ent.v_stockDaily.wh_name,
                        ent.v_stockDaily.group_name,
                        ent.v_stockDaily.brand_name,
                        func.sum(ent.v_stockDaily.qty).label('qty')
                        ) 
              .filter(
                        and_(
                              or_( ent.v_stockDaily.brand_id == brand_id ,brand_id == "",brand_id == "0" )
                            , or_( ent.v_stockDaily.group_id == categoty_id ,categoty_id == "",categoty_id == "0" )
                            , or_( ent.v_stockDaily.wh_id == wh_id ,wh_id == "",wh_id == "0" )
                            , or_( and_( ent.v_stockDaily.qty>0 , type_rp=="EXISTS" )
                                    , and_( ent.v_stockDaily.qty==0 , type_rp=="NONE"  )
                                    , and_(  type_rp==""  )
                                 )
                            )
                      ) 
              .group_by(ent.v_stockDaily.stock_date
                        ,ent.v_stockDaily.cc_id
                        ,ent.v_stockDaily.wh_id
                        ,ent.v_stockDaily.wh_name
                        ,ent.v_stockDaily.group_name
                        ,ent.v_stockDaily.brand_name
                        )           
              .order_by(ent.v_stockDaily.wh_name
                        ,ent.v_stockDaily.group_name
                        ,ent.v_stockDaily.brand_name)
              .offset(skip)
              .limit(limit)
              .all()
                )

    print(' row >>',len(result))

    return result

def getListGroupByModel(db: Session
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

    result = ( db.query(ent.v_stockDaily.cc_id,
                        ent.v_stockDaily.stock_date,
                        ent.v_stockDaily.wh_id,
                        ent.v_stockDaily.wh_name,
                        ent.v_stockDaily.group_name,
                        ent.v_stockDaily.brand_name,
                        ent.v_stockDaily.model_name,
                        func.sum(ent.v_stockDaily.qty).label('qty')
                        ) 
              .filter(
                        and_(
                              or_( ent.v_stockDaily.brand_id == brand_id ,brand_id == "",brand_id == "0" )
                            , or_( ent.v_stockDaily.group_id == categoty_id ,categoty_id == "",categoty_id == "0" )
                            , or_( ent.v_stockDaily.wh_id == wh_id ,wh_id == "",wh_id == "0" )
                            , or_( and_( ent.v_stockDaily.qty>0 , type_rp=="EXISTS" )
                                    , and_( ent.v_stockDaily.qty==0 , type_rp=="NONE"  )
                                    , and_(  type_rp==""  )
                                 )
                            )
                      ) 
              .group_by(ent.v_stockDaily.stock_date
                        ,ent.v_stockDaily.cc_id
                        ,ent.v_stockDaily.wh_id
                        ,ent.v_stockDaily.wh_name
                        ,ent.v_stockDaily.group_name
                        ,ent.v_stockDaily.brand_name
                        ,ent.v_stockDaily.model_name
                        )           
              .order_by(ent.v_stockDaily.wh_name
                        ,ent.v_stockDaily.group_name
                        ,ent.v_stockDaily.brand_name
                        ,ent.v_stockDaily.model_name
                        )
              .offset(skip)
              .limit(limit)
              .all()
                )

    print(' row >>',len(result))

    return result
