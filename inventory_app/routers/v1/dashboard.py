
import logging
import configparser

from datetime import timedelta, date

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import systemCheck, vstockcards as stk , stockcardBF , invoice as inv
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
        
        
@router.get("/dashboard/default")
async def default(   
                     wh_id: str
                   , doc_date_st: str = ""                   
                   , doc_date_en: str = ""                   
                   , cc_id:str=""       
                   , db: Session = Depends(get_db)):
    
    log.info('router-dashboard -> default')
    import datetime

    _date_st = datetime.datetime.strptime(doc_date_st, '%Y-%m-%d')
    _date_en = datetime.datetime.strptime(doc_date_en, '%Y-%m-%d')

    doc_date_last7day = datetime.datetime.strptime(doc_date_en, '%Y-%m-%d') + timedelta(days=-7)

    #print('>> doc_date_st ='+doc_date_st)    
    #print(doc_date_last7day)

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
 
    totalStock = stockcardBF.get_totalStock( db
                                      ,wh_id   
                                      ,2024
                                      ,cc_id
                                      )
 
    
    totalProblem = systemCheck.get_total_problem( db
                                      ,wh_id                                   
                                      ,cc_id
                                      )    
    
    result_daily_sale_bycust = stk.daily_sale_bycust( db
                                      ,wh_id
                                      ,doc_date_st
                                      ,doc_date_en                                    
                                      ,cc_id
                                      )

    result_SaleByOfficer = inv.get_SaleByOfficer( db
                                      ,wh_id
                                      ,_date_st
                                      ,_date_en                                    
                                      ,cc_id
                                      )     
    
    result_daily_sale_byDate = stk.daily_sale_byDate( db
                                      ,wh_id
                                      ,doc_date_last7day
                                      ,doc_date_en                                    
                                      ,cc_id
                                      ) 
        
    result_SaleByCategory = stk.daily_sale_byCategory( db
                                      ,wh_id
                                      ,doc_date_last7day
                                      ,doc_date_en                                    
                                      ,cc_id
                                      )     
    
    result_SaleByProdName = stk.daily_sale_byProdName( db
                                      ,wh_id
                                      ,doc_date_last7day
                                      ,doc_date_en                                    
                                      ,cc_id
                                      )         

    SaleByCategory_List = []
    for item in result_SaleByCategory :
        SaleByCategory_List.append({'group_name' : item[0], 'qty' : item[1], 'amt_price': item[2]})        

    SaleByProdName_List = []
    for item in result_SaleByProdName :
        SaleByProdName_List.append({'group_name' : item[0], 'pd_name' : item[1], 'qty' : item[2], 'amt_price': item[3]  } )        
    
    saleDailyByDate_list = []
    for item in result_daily_sale_byDate :
        saleDailyByDate_list.append({'doc_date' : item[0], 'qty' : item[1], 'qty_si': item[2], 'qty_iv': item[3], 'amt_cost': item[4], 'amt_price': item[5]  } )        
    
    saleCustlist = []
    for item in result_daily_sale_bycust :
        cust_name = item[1]
        if item[1].strip() =='' :
           cust_name = 'ไม่ระบุ' 
        saleCustlist.append( { 'cust_code' : item[0], 'cust_name' : cust_name, 'qty': item[2], 'amt_price': item[3]} )        
     
    saleOfficerlist = []
    for item in result_SaleByOfficer :
        saleOfficerlist.append( { 'user_id' : item[0], 'offier_name' : item[1], 'grand_total': item[2]  } )  

    # print(result_daily_sale_bycust)

    _sale_qty = 0 
    _sale_amt_cost = 0 
    _sale_amt_price = 0 

    _receive_qty = 0 
    _receive_amt_cost = 0 
    _receive_amt_price = 0 

    _inventory_qty = 0 
    _inventory_amt = 0

    if result_total_sale != [] :        
        _sale_qty = result_total_sale[0][1]
        _sale_amt_cost = result_total_sale[0][2]
        _sale_amt_price = result_total_sale[0][3]        
    print('=======================')
    
    if result_total_receive != [] :
        _receive_qty = result_total_receive[0][1]
        _receive_amt_cost = result_total_receive[0][2]
        _receive_amt_price = result_total_receive[0][3]
    
    print(totalStock[0][0])
    if totalStock[0][0] != None : 
        _inventory_qty = totalStock[0][0]
 
    if totalStock[0][0] != None :
        _inventory_amt = totalStock[0][1]


    result = {
               'sale_qty' : _sale_qty
              ,'sale_amt_cost' : _sale_amt_cost
              ,'sale_amt_price' : _sale_amt_price

              ,'receive_qty' : _receive_qty
              ,'receive_amt_cost' : _receive_amt_cost
              ,'receive_amt_price' : _receive_amt_price

              ,'inventory_qty' : _inventory_qty
              ,'inventory_amt' : _inventory_amt

              ,'problem_cnt' : totalProblem[0][0]

              ,'sale_daily_bycust' : saleCustlist
              ,'sale_daily_byofficer': saleOfficerlist
              ,'Sale_daily_bydate': saleDailyByDate_list

              ,'SaleByCategory': SaleByCategory_List
              ,'SaleByProdName': SaleByProdName_List
               }
    

    result_json = jsonable_encoder(result)    
    return JSONResponse(content=result_json, media_type="application/json")



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
                  