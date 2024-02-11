from sqlalchemy.orm import Session

from ..entity import brands as et_brand


def get_brand(db: Session, brand_name: str):
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
