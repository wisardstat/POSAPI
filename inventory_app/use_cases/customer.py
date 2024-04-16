from sqlalchemy.orm import Session
from ..entity import customer as et
from sqlalchemy import  and_ ,or_

def get_custSingle(db: Session, _cust_id: str):
    return db.query(et.TbCustomer).filter(et.TbCustomer.cust_id == _cust_id).first()

def get_custList(db: Session, skip: int = 0, limit: int = 100):

    result =  (
                db.query(et.TbCustomer)
                .filter(et.TbCustomer.cust_fname!="")
                .order_by(et.TbCustomer.cust_fname)
                .offset(skip)
                .limit(limit)
                .all()
                ) 
        
    return result 


def get_custListByName(db: Session,custFname:str, skip: int = 0, limit: int = 100):

    result =  (
                db.query(et.TbCustomer)
                .filter( and_( et.TbCustomer.cust_fname!=""
                              , 
                                or_(et.TbCustomer.cust_fname.ilike(f'%{custFname}%')
                                    ,custFname==''
                                    ) 
                              ) )
                .order_by(et.TbCustomer.cust_fname)
                .offset(skip)
                .limit(limit)
                .all()
                ) 
        
    return result 
 
 