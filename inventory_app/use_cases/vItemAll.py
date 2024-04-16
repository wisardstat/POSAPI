from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from ..entity import vItemAll as ent


def getSingle(db: Session, barcode: str,wh_id:str, cc_id: str):

    result = ( 
                db.query(ent.vItemAll)
                .filter( 
                        and_(  ent.vItemAll.cc_id == cc_id 
                             , ent.vItemAll.bar_code == barcode
                             , ent.vItemAll.wh_id == wh_id
                             ) 
                       ).first()
                )
    
    if (result==None) :
        print('>> Result is empty!! this is barcode is None.')
        result = []

    return result
