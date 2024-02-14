from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
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

def getListByDoc(db: Session
                  ,doc_date_st:str=""
                  ,doc_date_en:str=""
                  ,wh_id:str = ""                  
                  ,type_doc_id:str=""
                  
                  ,skip: int = 0
                  ,limit: int = 100):



    result = ( db.query(
                        ent.vstockcard.wh_name,
                        ent.vstockcard.doc_date,
                        ent.vstockcard.date_in,
                        ent.vstockcard.doc_id,
                        ent.vstockcard.type_doc,
                        ent.vstockcard.type_doc_id,
                        ent.vstockcard.cust_fname,

                        func.count(ent.vstockcard.doc_id).label("count"),
                        func.sum( ent.vstockcard.qty).label("qty"),
                        func.sum(func.abs( ent.vstockcard.qty*ent.vstockcard.cost )).label("amt_cost"),
                        func.sum(func.abs( ent.vstockcard.qty*ent.vstockcard.price )).label("amt_price"),                        
                      ) 
              .filter(
                        and_(                            
                              or_( ent.vstockcard.wh_id == wh_id ,wh_id == "",wh_id == "0" )
                            , or_(
                                  and_( ent.vstockcard.doc_date >= doc_date_st, ent.vstockcard.doc_date <= doc_date_en ),
                                  doc_date_st == "",
                                  doc_date_st == "0",
                              )
                             , or_(
                                  ent.vstockcard.type_doc_id == type_doc_id,
                                  type_doc_id == "",
                                  type_doc_id == "0",
                              ), 
                            )
                      )   
              .group_by(
                        ent.vstockcard.wh_name,
                        ent.vstockcard.date_in,
                        ent.vstockcard.doc_date,
                        ent.vstockcard.doc_id,
                        ent.vstockcard.type_doc,
                        ent.vstockcard.type_doc_id,
                        ent.vstockcard.cust_fname,
                )           
              .order_by(ent.vstockcard.doc_date
                        ,ent.vstockcard.wh_name                        
                        ,ent.vstockcard.doc_id
                        )
              .offset(skip)
              .limit(limit)
              .all()
                )

    print(' row >>',len(result))

    return result


def getListByDoc_Total(db: Session
                  , doc_date_st:str = ""   
                  , doc_date_en:str = ""   
                  ,wh_id:str = ""                  
                  ,type_doc_id:str=""                  
                  ,skip: int = 0
                  ,limit: int = 100):



    result = ( db.query(
                        func.count(ent.vstockcard.doc_id).label("count"),
                        func.sum(func.abs( ent.vstockcard.qty)).label("qty"),
                        func.sum(func.abs( ent.vstockcard.qty*ent.vstockcard.cost )).label("amt_cost"),
                        func.sum(func.abs( ent.vstockcard.qty*ent.vstockcard.price )).label("amt_price"),                        
                      ) 
              .filter(
                        and_(                            
                              or_( ent.vstockcard.wh_id == wh_id ,wh_id == "",wh_id == "0" )
                            , or_(
                                  and_( ent.vstockcard.doc_date >= doc_date_st, ent.vstockcard.doc_date <= doc_date_en ),
                                  doc_date_st == "",
                                  doc_date_st == "0",
                              )
                             , or_(
                                  ent.vstockcard.type_doc_id == type_doc_id,
                                  type_doc_id == "",
                                  type_doc_id == "0",
                              ), 
                            )
                      )                               
              .first()
                )

    print(' row >>',len(result))

    return result
