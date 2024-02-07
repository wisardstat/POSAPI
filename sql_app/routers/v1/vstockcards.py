
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
async def get_vstockcard_list_report(brand_id:str = "", skip: int = 0, limit: int = 10, db: Session = Depends(get_db))-> List[dtos.vstockcard]:
    
    print('*************************')
    print(' >> get_vstockcard_list_report ')
    print(' brand_id =',brand_id)

    vstockcard = usecase.getListReport(db, brand_id =brand_id
                                                    , skip=skip, limit=limit)
    return vstockcard


        