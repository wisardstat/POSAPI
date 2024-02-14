
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import vstockcards as usecase
from ...dtos import vstockcards as dtos
from ...loggings import  log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/vstockcard/getVstockcardListAll")
async def getVstockcardListAll(skip: int = 0, limit: int = 10, db: Session = Depends(get_db))-> List[dtos.vstockcard]:

    log.info('router-vstockcard -> getVstockcardListAll')

    vstockcard = usecase.getListAll(db, skip=skip, limit=limit)
    return vstockcard

@router.get("/vstockcard/getListByDoc")
async def getListByDoc( 
                         doc_date_st:str=""
                        ,doc_date_en:str=""
                        ,wh_id:str = ""                                                
                        ,type_doc_id:str = ""                        
                        ,skip: int = 0, limit: int = 100
                        ,db: Session = Depends(get_db))-> List[dtos.vstockcard_getListByDoc]:
    
    log.info('router-vstockcard -> getListByDoc')        
    log.info('router-vstockcard -> wh_id ='+str(wh_id))
    log.info('router-vstockcard -> type_doc_id ='+str(type_doc_id))
    log.info('router-vstockcard -> skip ='+str(skip))
    log.info('router-vstockcard -> limit ='+str(limit))
    log.info('router-vstockcard -> doc_date ='+str(doc_date_st))

    vstockcard = usecase.getListByDoc(db
                                        , doc_date_st=doc_date_st
                                        , doc_date_en=doc_date_en
                                        , wh_id = wh_id
                                        , type_doc_id =type_doc_id                                       
                                        , skip=skip
                                        , limit=limit)
    return vstockcard


@router.get("/vstockcard/getListByDoc_Total")
async def getListByDoc_Total( 
                         doc_date_st:str=""
                        ,doc_date_en:str=""
                        ,wh_id:str = ""                                                
                        ,type_doc_id:str = ""                        
                        ,skip: int = 0, limit: int = 100
                        ,db: Session = Depends(get_db))-> dtos.vstockcard_getListByDoc_Total:
    
    log.info('router-vstockcard -> getListByDoc_Total')        
    log.info('router-vstockcard -> wh_id ='+str(wh_id))
    log.info('router-vstockcard -> type_doc_id ='+str(type_doc_id))
    log.info('router-vstockcard -> skip ='+str(skip))
    log.info('router-vstockcard -> limit ='+str(limit))
    log.info('router-vstockcard -> doc_date_st ='+str(doc_date_st))
    log.info('router-vstockcard -> doc_date_en ='+str(doc_date_en))

    vstockcard = usecase.getListByDoc_Total(db
                                        , doc_date_st=doc_date_st
                                        , doc_date_en=doc_date_en
                                        , wh_id = wh_id
                                        , type_doc_id =type_doc_id                                       
                                        , skip=skip
                                        , limit=limit)
    return vstockcard


        
        