
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

@router.get("/vstockcard/getVstockardListReport")
async def getVstockardListReport(wh_id:str = ""
                                     ,categoty_id:str = ""
                                     ,brand_id:str = ""
                                     ,type_rp:str = ""
                                     ,skip: int = 0, limit: int = 100, db: Session = Depends(get_db))-> List[dtos.vstockcard]:
    
    log.info('router-vstockcard -> getVstockardListReport')
    log.info('router-vstockcard -> brand_id =',brand_id)
    log.info('router-vstockcard -> categoty_id =',categoty_id)
    log.info('router-vstockcard -> wh_id =',wh_id)
    log.info('router-vstockcard -> type_rp =',type_rp)
    log.info('router-vstockcard -> skip =',skip)
    log.info('router-vstockcard -> limit =',limit)

    vstockcard = usecase.getListReport(db
                                        , wh_id = wh_id
                                        , categoty_id = categoty_id
                                        , brand_id =brand_id
                                        , type_rp =type_rp
                                        , skip=skip
                                        , limit=limit)
    return vstockcard


        