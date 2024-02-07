
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import brands as uc_brands
from ...dtos import brands as dt_brand


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/brand/")
async def read_brand(skip: int = 0, limit: int = 100, db: Session = Depends(get_db))-> List[dt_brand.brand]:
    brand = uc_brands.get_brand(db, skip=skip, limit=limit)
    return brand

        