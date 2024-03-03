import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

# from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import brands as uc_brands
from ...dtos import brands as dt_brand
from ...loggings import log

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/brand/")
async def read_brand(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[dt_brand.brand]:
    print(">> read_brand")

    log.info("info-router-brand -> read_brand")
    brand = uc_brands.get_brand(db, skip=skip, limit=limit)
    return brand


@router.post("/brand/add", response_model=dt_brand.brand)
def create_brand(bd: dt_brand.brandCreate,
                      db: Session = Depends(get_db)):

    log.info("router-brand -> create_warehouse")

    print('brand_name==>',bd.brand_name)
    
    db_brand = uc_brands.get_brand_single(db, brand_name = bd.brand_name)
    
    if db_brand:                
        print("Error!!! ==> brand_name have existed ")
        
        raise HTTPException(status_code=400, detail="Brand have existed !!")
        log.error("router-brand -> brand have existed !!")
        
    print('+++ ADD +++')
    return uc_brands.create_brand(db=db, brand=bd)
