
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import supply as uc_supply
from ...dtos import supply as dt_supply
from ...loggings import log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
     
 
@router.get("/supply/list")
async def getlist(   find_name:str="",skip: int = 0, limit: int = 100
                    , db: Session = Depends(get_db)
) -> List[dt_supply.supply]:
    
    print(">> user/ getlist")
    log.info("info-router-user -> user/ getlist")

    result = uc_supply.get_list(db,find_name=find_name, skip=skip, limit=limit)
    print('++++++++++++++++++++++++++++++++')
    return result 


@router.get("/supply/single")
async def getSingle_byId( Supply_id:str, db: Session = Depends(get_db)
                  ) -> dt_supply.supply:
    
    print(">> user/ get_single")
    log.info("info-router-user -> user/ get_single")

    result = uc_supply.getSingle_byId(db,Supply_id=Supply_id)
    
    if (result==None):    
        print('+++ None data !! +++')      
        result=[]
    
    return result         