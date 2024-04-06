
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import user as uc_user
from ...dtos import user as dt_user
from ...loggings import log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/user/")
async def get_user_single(user: str , password: str
                 , db: Session = Depends(get_db))-> List[dt_user.user]:
    
    print('+++++++++++++++++++++++++++++++++++')
    print('>> router-user -> get_user_single')

    user = uc_user.get_user_single(db, user=user, password=password)
    return user
 
 
        