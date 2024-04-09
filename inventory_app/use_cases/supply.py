from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import  and_ ,or_
from ..entity import   tbSupply


 
def get_list(db: Session,find_name:str='', skip: int = 0, limit: int = 10):

    result = (
        db.query(tbSupply.TbSupply)
        .filter( 
                or_(tbSupply.TbSupply.supply_name.ilike(f'%{find_name}%')
                     ,find_name==''
                     ) 
                )
        .order_by(tbSupply.TbSupply.supply_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return result

 
def getSingle_byId(db: Session,Supply_id:str):

    result = (
        db.query(tbSupply.TbSupply)
        .filter( tbSupply.TbSupply.supply_id==Supply_id )
        .first()
    )

    return result