from sqlalchemy.orm import Session
from ..entity import categories as et_cat


def get_category_byName(db: Session, group_name : str):
    return db.query(et_cat.tbcategory).filter(et_cat.tbcategory.group_name == group_name).first()

def get_category_byId(db: Session, group_id : str):
    return db.query(et_cat.tbcategory).filter(et_cat.tbcategory.group_id == group_id).first()

def get_category_list(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(et_cat.tbcategory)
        .order_by(et_cat.tbcategory.group_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_category_emei_list(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(et_cat.tbcategory)
        .filter(et_cat.tbcategory.group_emei=="Y")
        .order_by(et_cat.tbcategory.group_name)
        .offset(skip)
        .limit(limit)
        .all()
    )
