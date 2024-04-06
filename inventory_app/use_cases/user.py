from sqlalchemy.orm import Session

from ..dtos import user as dt
from ..entity import user as et_user


def get_user_single(db: Session, user: str, password: str):

    print('==> get_user_single /user=',user,'/password=',password)

    return (
        db.query(et_user.User)       
        .first()
    )
