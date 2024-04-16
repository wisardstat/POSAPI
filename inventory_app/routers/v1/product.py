
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import vItemAll as uc
from ...dtos import vItemAll as dt
from ...loggings import log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/product_info/Barcode")
async def getProductInfo( barcode:str, wh_id:str, cc_id:str
                     , db: Session = Depends(get_db))-> dt.vItemAll:
    
    print('>> getProductInfo')
    log.info('product / getProductInfo ')
    result = uc.getSingle(db,barcode,wh_id,cc_id)
    print('>> getProductInfo-end ')
    return result 
                