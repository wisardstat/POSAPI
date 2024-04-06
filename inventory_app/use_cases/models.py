from sqlalchemy.orm import Session
from ..entity import models as et_model


def get_model(db: Session, model_name: str):
    return db.query(et_model.TbModel).filter(et_model.TbModel.model_name == model_name).first()

def get_model_list(db: Session, skip: int = 0, limit: int = 100):

    result =  (
        db.query(et_model.TbModel)
        .order_by(et_model.TbModel.model_name)
        .offset(skip)
        .limit(limit)
        .all()
    ) 
 
    return result 

def get_model_list_byBrand(db: Session,group_id:str,brand_id:str, skip: int = 0, limit: int = 100):

    result =  (
        db.query(et_model.TbModel)        
        .filter(  (et_model.TbModel.group_id==group_id)
                    ,(et_model.TbModel.brand_id==brand_id)
                    )
        .order_by(et_model.TbModel.model_name)
        .offset(skip)
        .limit(limit)
        .all()
    ) 
 
    return result 