
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

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

    print('==================================')
    print( '>> Get Password : '+password )

    enc = password
    key = "d2dpos@topgunner"
    iv =  'd2d@linkin#park!'.encode('utf-8') #16 char for AES128

    enc = base64.b64decode(enc)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    password_decryption = unpad(cipher.decrypt(enc),16).decode('utf-8')
    
    print( 'Password : '+password_decryption )

    result = uc_user.get_single(db,user,password_decryption)
    
    if (result==None):    
        print('+++ None data !! +++')      
        result=[]
    
    return result 
        
@router.get("/user/branch")
async def get_BranchList( user_id:str, 
                         db: Session = Depends(get_db) ) -> List[dt_user.user_branch]:
    
    print(">> user/ get_single")
    log.info("info-router-user -> user/ get_BranchList")

    result = uc_user.getBranch_list(db,user_id)
    
    print(len(result))

    if (result==None):    
        print('>> get_BranchList')
        print('>> None data !! +++')      
        result=[]
    
    return result 
        