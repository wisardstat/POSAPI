
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import vstockcards as usecase
from ...dtos import vstockcards as dtos


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/vstockcard/")
async def get_vstockcard_list_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db))-> List[dtos.vstockcard]:
    vstockcard = usecase.getListAll(db, skip=skip, limit=limit)
    return vstockcard

@router.get("/vstockcard/report")
async def get_vstockcard_list_report(wh_id:str = ""
                                     ,categoty_id:str = ""
                                     ,brand_id:str = ""
                                     ,type_rp:str = ""
                                     ,skip: int = 0, limit: int = 100, db: Session = Depends(get_db))-> List[dtos.vstockcard]:
    
    print('*************************')
    print(' >> get_vstockcard_list_report ')
    print(' brand_id =',brand_id)
    print(' categoty_id =',categoty_id)

    vstockcard = usecase.getListReport(db
                                        , wh_id = wh_id
                                        , categoty_id = categoty_id
                                        , brand_id =brand_id
                                        , type_rp =type_rp
                                        , skip=skip
                                        , limit=limit)
    return vstockcard


        