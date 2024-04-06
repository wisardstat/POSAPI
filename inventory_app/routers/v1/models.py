
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import models as uc_model
from ...dtos import models as dt_model
from ...loggings import log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/model/list")
async def getList(skip: int = 0
                     , limit: int = 100
                     , db: Session = Depends(get_db))-> List[dt_model.model]:
    
    log.info('router-Model -> read_model')
    model = uc_model.get_model_list(db, skip=skip, limit=limit)
    return model

@router.get("/model/list/ByBrand")
async def getList_byBrand( group_id:str,brand_id:str
                    , skip: int = 0 , limit: int = 100
                    , db: Session = Depends(get_db))-> List[dt_model.model]:
    
    log.info('router-Model -> read_model')
    model = uc_model.get_model_list_byBrand(db,group_id,brand_id, skip, limit)
    return model

        