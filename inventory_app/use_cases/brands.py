from sqlalchemy.orm import Session
from ..dtos import brands as dt

from ..entity import brands as et_brand

def create_brand(db: Session, brand: dt.brandCreate):
    
    db_brand = et_brand.TbBrand(
                            brand_id=brand.brand_id,
                            brand_name=brand.brand_name,                            
                            cc_id=brand.cc_id
                            )
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

def get_brand_single(db: Session, brand_name: str):
    return (
        db.query(et_brand.TbBrand)
        .filter(et_brand.TbBrand.brand_name == brand_name)
        .first()
    )


def get_brand(db: Session, skip: int = 0, limit: int = 10):

    result = (
        db.query(et_brand.TbBrand)
        .order_by(et_brand.TbBrand.brand_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return result
