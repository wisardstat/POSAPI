from sqlalchemy.orm import Session
from ..entity import models as et_model


def get_genid(db: Session, model_name: str):
    return db.query(et_model.TbModel).filter(et_model.TbModel.model_name == model_name).first()

def getNewCode(db: Session,TypeId:str,Frm:str ,format:str ,type_form:str , _cc_id:str ,skip: int = 0, limit: int = 10):

    result =  (
        db.query(et_model.TbModel)
        .order_by(et_model.TbModel.model_name)
        .offset(skip)
        .limit(limit)
        .all()
    ) 
 
    return result 