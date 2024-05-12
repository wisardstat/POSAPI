from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, func , Integer
from ..entity import   tbstockcardbf as ent


 
def get_totalStock(db: Session,wh_id:str, zyear: int = 9999 , cc_id:str='A01'):

 
    result = (
                db.query(                            
                        func.sum(func.abs( ent.stockcardBF.qty)).label("qty")
                        ,func.sum(func.abs(ent.stockcardBF.amt)).label("amt")
                    )
                .filter(
                        and_( ent.stockcardBF.zyear == zyear
                            ,ent.stockcardBF.wh_id == wh_id 
                            ,ent.stockcardBF.cc_id == cc_id 
                            ) 
                        )
                .all()
            )

    return result

  