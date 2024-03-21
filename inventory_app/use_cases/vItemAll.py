from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from ..entity import vItemAll as ent


def getSingle(db: Session, barcode: str, cc_id: str):
    return db.query(ent.vItemAll).filter(ent.vItemAll.cc_id == cc_id,ent.vItemAll.bar_code == barcode).first()
