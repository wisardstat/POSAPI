from sqlalchemy.orm import Session
from sqlalchemy import  and_ ,or_
from ..dtos import user as dt
from ..entity import user as et_user ,userBranch 


def get_list(db: Session, skip: int = 0, limit: int = 10):

    print('>>> _user - get_list')
    result = (
        db.query(et_user.User)
        .order_by(et_user.User.user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return result

def get_single(db: Session
               ,_user:str,_password:str):

    print('>>> _user=',_user)
    result = (

        db.query(et_user.User)
        .filter( 
                and_(  et_user.User.user_login==_user , 
                      et_user.User.user_password==_password)
             )
        .first()
    )

    return result

def get_singleById(db: Session
               ,user_id:str):

    print('>>> get_singleById ', user_id)
    result = (
                db.query(et_user.User)
                .filter( et_user.User.user_id == user_id )
                .first()
             )

    return result
 

def getBranch_list(db: Session ,_user_id :str ):

    result = (
                db.query(userBranch.UserBranch)                
                .filter(
                        (userBranch.UserBranch.user_id==_user_id)                        
                        )
                .limit(10)       
                .all()
              )

    return result
