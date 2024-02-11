from sqlalchemy.orm import Session
from ..entity import models as et_model


def get_model(db: Session, model_name: str):
    return db.query(et_model.TbModel).filter(et_model.TbModel.model_name == model_name).first()

def get_model_list(db: Session, skip: int = 0, limit: int = 10):

    result =  (
        db.query(et_model.TbModel)
        .order_by(et_model.TbModel.model_name)
        .offset(skip)
        .limit(limit)
        .all()
    ) 
 
    return result 