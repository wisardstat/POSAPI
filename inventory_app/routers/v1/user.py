
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import user as uc_user
from ...dtos import user as dt_user, user_branch as ubranch
from ...loggings import log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
     
 
@router.get("/user/list")
async def getlist(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[dt_user.user]:
    
    print(">> user/ getlist")
    log.info("info-router-user -> user/ getlist")

    result = uc_user.get_list(db, skip=skip, limit=limit)
    print('++++++++++++++++++++++++++++++++')
    return result 

@router.get("/user/single")
async def get_single( user:str='wisard',password:str='wds6597', db: Session = Depends(get_db) ) -> dt_user.user:
    
    print(">> user/ get_single")
    log.info("info-router-user -> user/ get_single")

    result = uc_user.get_single(db,user,password)
    
    if (result==None):    
        print('+++ None data !! +++')      
        result=[]
    
    return result 
        
@router.get("/user/branch")
async def get_BranchList( user_id:str, db: Session = Depends(get_db) ) -> List[ubranch.userBranch]:
    
    print(">> user/ get_single")
    log.info("info-router-user -> user/ get_BranchList")

    result = uc_user.getBranch_list(db,user_id)
    
    print(len(result))

    if (result==None):    
        print('>> get_BranchList')
        print('>> None data !! +++')      
        result=[]
    
    return result 
        