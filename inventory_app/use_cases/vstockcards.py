from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func , Integer
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

#***********************************  By-Document *****************************************#

def getListByDoc(  db: Session
                  ,doc_date_st:str=""
                  ,doc_date_en:str=""
                  ,wh_id:str = ""                  
                  ,type_doc_id:str=""
                  ,find_cust_name:str = ""                        
                  ,skip: int = 0
                  ,limit: int = 100):

    result = ( db.query(
                        ent.vstockcard.wh_name,
                        ent.vstockcard.doc_date,
                        
                        ent.vstockcard.doc_id,
                        ent.vstockcard.type_doc,
                        ent.vstockcard.type_doc_id,
                        ent.vstockcard.cust_fname,
                        func.right( ent.vstockcard.doc_id,2).label("row_key"),                        
                        func.count(ent.vstockcard.doc_id.distinct()).label("count"),
                        func.sum( ent.vstockcard.qty).label("qty"),
                        func.max(ent.vstockcard.date_in).label("date_in"),
#                         func.sum(func.abs( ent.vstockcard.qty*ent.vstockcard.cost )).label("amt_cost"),
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
                              ) 
                             , or_(
                                  ent.vstockcard.cust_fname.ilike(f'%{find_cust_name}%'),
                                  find_cust_name == "",
                                  find_cust_name == "0",
                              ), 
                            )
                      )   
              .group_by(
                        ent.vstockcard.wh_name,
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
                      ,doc_date_st:str = ""   
                      ,doc_date_en:str = ""   
                      ,wh_id:str = ""                  
                      ,type_doc_id:str=""    
                      ,find_cust_name:str = ""                                      
                      ,skip: int = 0
                      ,limit: int = 100):

    result = ( db.query(
                        func.count(ent.vstockcard.doc_id.distinct()).label("count"),
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
                              ) 
                               , or_(
                                  ent.vstockcard.cust_fname.ilike(f'%{find_cust_name}%'),
                                  find_cust_name == "",
                                  find_cust_name == "0",
                              ), 
                            )
                      ).first()
                )

    print(' row >>',len(result))

    return result

#***********************************  By-item *****************************************#

def getListByItem(  db: Session
                  ,doc_date_st:str=""
                  ,doc_date_en:str=""
                  ,wh_id:str = ""                  
                  ,type_doc_id:str=""

                  ,group_id:str=""
                  ,brand_id:str=""
                  ,model_id:str=""

                  ,find_cust_name:str = ""                        
                  ,find_pd_name:str = ""                        
                  ,skip: int = 0
                  ,limit: int = 100):

    result = ( db.query(
                        ent.vstockcard.wh_name,
                        ent.vstockcard.doc_date,
                        ent.vstockcard.date_in,
                        ent.vstockcard.doc_id,
                        ent.vstockcard.type_doc,
                        ent.vstockcard.type_doc_id,
                        ent.vstockcard.group_name,
                        ent.vstockcard.brand_name,
                        ent.vstockcard.model_name,
                        ent.vstockcard.pd_name,
                        ent.vstockcard.cust_fname,
                        func.right( ent.vstockcard.doc_id,2).label("row_key"),                        
                        func.count(ent.vstockcard.doc_id.distinct()).label("count"),
                        func.sum( ent.vstockcard.qty).label("qty"),
                        func.sum(func.abs( ent.vstockcard.qty)).label("qty_abs"),
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
                              ) 
                             , or_(
                                  ent.vstockcard.cust_fname.ilike(f'%{find_cust_name}%'),
                                  find_cust_name == "",
                                  find_cust_name == "0",
                              ) 
                               , or_(
                                  ent.vstockcard.pd_name.ilike(f'%{find_pd_name}%'),
                                  find_pd_name == "",
                                  find_pd_name == "0",
                              ) 
                            , or_(
                                  ent.vstockcard.group_id == group_id,
                                  group_id == "",
                                  group_id == "0",
                              ) 
                              , or_(
                                  ent.vstockcard.brand_id == brand_id,
                                  brand_id == "",
                                  brand_id == "0",
                              ) 
                               , or_(
                                  ent.vstockcard.model_id == model_id,
                                  model_id == "",
                                  model_id == "0",
                              )
                            )
                      )   
              .group_by(
                        ent.vstockcard.wh_name,
                        ent.vstockcard.doc_date,
                        ent.vstockcard.date_in,
                        ent.vstockcard.doc_id,
                        ent.vstockcard.type_doc,
                        ent.vstockcard.type_doc_id,
                        ent.vstockcard.group_name,
                        ent.vstockcard.brand_name,
                        ent.vstockcard.model_name,
                        ent.vstockcard.pd_name,
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



def getListByItem_Total(  db: Session
                  ,doc_date_st:str=""
                  ,doc_date_en:str=""
                  ,wh_id:str = ""                  
                  ,type_doc_id:str=""

                  ,group_id:str=""
                  ,brand_id:str=""
                  ,model_id:str=""

                  ,find_cust_name:str = ""                        
                  ,find_pd_name:str = ""                        
                  ,skip: int = 0
                  ,limit: int = 100):

    result = ( db.query(                                               
                        func.count(ent.vstockcard.doc_id.distinct()).label("count"),
                        func.sum( ent.vstockcard.qty).label("qty"),
                        func.sum(func.abs( ent.vstockcard.qty)).label("qty_abs"),
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
                              ) 
                             , or_(
                                  ent.vstockcard.cust_fname.ilike(f'%{find_cust_name}%'),
                                  find_cust_name == "",
                                  find_cust_name == "0",
                              ) 
                               , or_(
                                  ent.vstockcard.pd_name.ilike(f'%{find_pd_name}%'),
                                  find_pd_name == "",
                                  find_pd_name == "0",
                              ) 
                            , or_(
                                  ent.vstockcard.group_id == group_id,
                                  group_id == "",
                                  group_id == "0",
                              ) 
                              , or_(
                                  ent.vstockcard.brand_id == brand_id,
                                  brand_id == "",
                                  brand_id == "0",
                              ) 
                               , or_(
                                  ent.vstockcard.model_id == model_id,
                                  model_id == "",
                                  model_id == "0",
                              )
                            )
                      ).first()
                )

    print(' row >>',len(result))

    return result
