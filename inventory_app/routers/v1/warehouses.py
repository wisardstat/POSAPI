
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import warehouses as usecase
from ...dtos import warehouses as dtos
from ...loggings import  log

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/warehouse/")
async def read_warehouses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db))-> List[dtos.warehouse]:

    log.info('router-warehouses -> read_warehouses')

    warehouses = usecase.get_warehouse(db, skip=skip, limit=limit)
    return warehouses

@router.post("/warehouses/add", response_model=dtos.warehouse)
def create_warehouse(wh: dtos.warehouseCreate, db: Session = Depends(get_db)):    
    
    log.info('router-warehouses -> create_warehouse')

    db_wh = usecase.get_warehouse_single(db,wh_name=wh.wh_name)
    if db_wh:
        raise HTTPException(status_code=400, detail="Inventory have existed !!")
        log.error('router-warehouses -> Inventory have existed !!')
    
    return usecase.create_warehouse(db=db, wh=wh)        