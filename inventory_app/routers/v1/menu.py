import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import menu
from ...loggings import log
from ...utility import apiResponse

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.get('/menus')
def get_menus(group_user_id:str, 
                         db: Session = Depends(get_db)):
    
    menus = menu.get_menus_by_group_user_id(db, group_user_id)
    return apiResponse.response(200,status="success",data=menus,message="")
    
