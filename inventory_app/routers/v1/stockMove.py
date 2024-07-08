import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

# from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import stockMove as uc_stockIn ,stockCard as uc_stockCard
from ...dtos import stockMove
from ...loggings import log
from ...utility import genidrandom , apiResponse

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/stockmove/add")
def stockin_add(request: stockMove.StockMoveRequest,
                      db: Session = Depends(get_db)):
    print('************************************************')
    print('Start - Move Stock')
    print('************************************************')
         
    print('*******  generate_id_random - StockMOV *********')
    request.doc_id = genidrandom.generate_id_random(db,"StockMove", "MO", 10000, "yearmonth", request.cc_id)
    
    print('*******  Loop for - insert stock move header / stock move detail *********')
    for item in request.itemList:
        
        item.doc_id = request.doc_id
        print('*******  Add Stock Move Header  *********')
        uc_stockIn.add_stockMov_h(db,request)
        
        print('*******  Add Stock Move Header  *********')
        uc_stockIn.add_stockMov_d(db,item)
        
        print('*******  Add Stock Card MO  *********')
        request.type_doc = "MO"
        item.wh_id = request.wh_from
        uc_stockCard.add_StockMoveCard(db,request,item)
        
        print('*******  Add Stock Card MI  *********')
        request.type_doc = "MI"
        item.wh_id = request.wh_target
        uc_stockCard.add_StockMoveCard(db,request,item)
    
    
    return apiResponse.response(200, status="success", message="")