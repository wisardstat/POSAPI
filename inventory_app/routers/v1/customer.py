
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import customer as uc
from ...dtos import customer as dt
from ...loggings import log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/customer/list")
async def getList(skip: int = 0
                     , limit: int = 100
                     , db: Session = Depends(get_db))-> List[dt.customer]:
    
    log.info('router-Customer -> getList ')
    result = uc.get_custList(db, skip=skip, limit=limit)
    return result

@router.get("/customer/id")
async def getSingle( cust_id:str
                     , db: Session = Depends(get_db))-> dt.customer:
    
    log.info('router-Customer -> getSingle ')
    result = uc.get_custSingle(db,cust_id)
    return result 

@router.get("/customer/Fname")
async def getListByFname( cust_fname:str
                     , db: Session = Depends(get_db))-> List[dt.customer]:
    
    log.info('router-Customer -> getSingle ')
    result = uc.get_custListByName(db,cust_fname)
    return result 
                