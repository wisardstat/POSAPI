from sqlalchemy.orm import Session
from ..entity import warehouses as ent
from ..dtos import warehouses as schemas


def get_warehouse_single(db: Session, wh_name: str):    
    return db.query(ent.tbwareHouse).filter(ent.tbwareHouse.wh_name == wh_name).first()

def get_warehouse(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(ent.tbwareHouse)
        .order_by(ent.tbwareHouse.wh_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

def create_warehouse(db: Session, wh: schemas.warehouseCreate):
    
    db_wh = ent.tbwareHouse(
                            wh_id=wh.wh_id,
                            wh_name=wh.wh_name,
                            wh_group=wh.wh_group,
                            cc_id=wh.cc_id
                            )
    db.add(db_wh)
    db.commit()
    db.refresh(db_wh)
    return db_wh