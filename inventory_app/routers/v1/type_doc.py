import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

# from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import type_doc as uc
from ...dtos import type_doc as dt
from ...loggings import log

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/type_doc/getList")
async def getList(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[dt.type_doc_list]:
    print(">> read_brand")

    log.info("info-router-type_doc -> read_type_doc")
    brand = uc.getList(db, skip=skip, limit=limit)
    return brand
