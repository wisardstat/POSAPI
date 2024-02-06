
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends, FastAPI, HTTPException

#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import categories as usecase
from ...dtos import categories as dtos

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/category/")
async def read_category(skip: int = 0, limit: int = 10, db: Session = Depends(get_db))-> List[dtos.categories]:
    category = usecase.get_category_list(db, skip=skip, limit=limit)
    return category
