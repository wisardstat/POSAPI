
import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import vstockcards as stk
from ...dtos import vstockcards as dtstk
from ...loggings import log

from ...utility import apiResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/dashboard/daily_total")
async def daily_total(   wh_id: str
                   , doc_date_st: str = ""
                   , doc_date_en: str = ""
                   , cc_id:str=""       
                   , db: Session = Depends(get_db)):
    
    log.info('router-dashboard -> daily')

    result_total_sale = stk.daily_total_sale( db
                                      ,wh_id
                                      ,doc_date_st
                                      ,doc_date_en
                                      ,'IV'
                                      ,cc_id
                                      )
    result_total_receive = stk.daily_total_sale( db
                                      ,wh_id
                                      ,doc_date_st
                                      ,doc_date_en
                                      ,'SI'
                                      ,cc_id
                                      )
 
 

    result = {
               'sale_qty' : result_total_sale[0][1]
              ,'sale_amt_cost' : result_total_sale[0][2]
              ,'sale_amt_price' : result_total_sale[0][3]

              ,'receive_qty' : result_total_receive[0][1]
              ,'receive_amt_cost' : result_total_receive[0][2]
              ,'receive_amt_price' : result_total_receive[0][3]

               }
    

    result_json = jsonable_encoder(result)    
    return JSONResponse(content=result_json, media_type="application/json")


@router.get("/dashboard/daily_bycust")
async def daily_bycust(   wh_id: str
                   , doc_date_st: str = ""
                   , doc_date_en: str = ""
                   , cc_id:str=""       
                   , db: Session = Depends(get_db))->List[dtstk.daily_bycust]:
    
    log.info('router-dashboard -> daily')

    result = stk.daily_sale_bycust( db
                                      ,wh_id
                                      ,doc_date_st
                                      ,doc_date_en                                    
                                      ,cc_id
                                      ) 
      
    return result

@router.get("/dashboard/daily_bydate")
async def daily_byDate(   wh_id: str
                   , doc_date_st: str = ""
                   , doc_date_en: str = ""
                   , cc_id:str=""       
                   , db: Session = Depends(get_db))->List[dtstk.daily_bydate]:
    
    log.info('router-dashboard -> daily')

    result = stk.daily_sale_byDate( db
                                      ,wh_id
                                      ,doc_date_st
                                      ,doc_date_en                                    
                                      ,cc_id
                                      ) 
      
    return result


@router.get("/dashboard/daily_bycategory")
async def daily_byCategory(   wh_id: str
                   , doc_date_st: str = ""
                   , doc_date_en: str = ""
                   , cc_id:str=""       
                   , db: Session = Depends(get_db))->List[dtstk.daily_bycategory]:
    
    log.info('router-dashboard -> daily')

    result = stk.daily_sale_byCategory( db
                                      ,wh_id
                                      ,doc_date_st
                                      ,doc_date_en                                    
                                      ,cc_id
                                      ) 
      
    return result
          
@router.get("/dashboard/daily_bybrand")
async def daily_bybrand(   wh_id: str
                   , doc_date_st: str = ""
                   , doc_date_en: str = ""
                   , cc_id:str=""       
                   , db: Session = Depends(get_db))->List[dtstk.daily_bybrand]:
    
    log.info('router-dashboard -> daily')

    result = stk.daily_sale_bybrand( db
                                      ,wh_id
                                      ,doc_date_st
                                      ,doc_date_en                                    
                                      ,cc_id
                                      ) 
      
    return result
                  