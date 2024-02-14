from sqlalchemy.orm import Session

from ..entity import type_doc as et
 


def getList(db: Session, skip: int = 0, limit: int = 10):

    result = (
        db.query(et.type_doc)
        .order_by(et.type_doc.type_doc_name)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return result
