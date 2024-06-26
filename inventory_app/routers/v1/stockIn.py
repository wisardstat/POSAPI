import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

# from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import stockIn as uc_stockIn , categories as uc_categories , vItemAll as uc_vitemall ,productM as uc_productM , productUnit as uc_productUnit , stockCard as uc_stockCard
from ...dtos import stockIn , categories
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


@router.post("/stockin/add")
def stockin_add(request: stockIn.StockInRequest,
                      db: Session = Depends(get_db)):
    
    print('************************************************')
    print('Start - Save Stock-in')
    print('************************************************')

    print('==> request.vendor_id==',request.vendor_id)
    # stockIn_h : stockIn.StockInRequest
    stockIn_d : List[stockIn.StockItem] = []
    alert = ""    
    print('*******  generate_id_random - StockIn *********')
    request.doc_id = genidrandom.generate_id_random(db,"StockIN", "SI", 10000, "yearmonth", request.cc_id)
    
    print('*******  Add Stock in Header  *********')
    uc_stockIn.add_stockIn_h(db,request) 

    if (request.vendor_id is None or request.vendor_id=="") :
        print('==> add_supply')
        print(f"==> vendor_id: {request.vendor_id}")
        
        print('*******  generate_id_random - supply_id *********')
        request.supplierDetail.supply_id = genidrandom.generate_id_random(db,"SUPPLYID", "S", 1000, "zero", request.cc_id)
        request.vendor_id = request.supplierDetail.supply_id
        print(f"==> SUPPLYID: {request.supplierDetail.supply_id}")

        uc_stockIn.add_supply(db,request.supplierDetail)
    else:
        print('==> update_supply')
        print(f"==> vendor_id: {request.vendor_id}")
        uc_stockIn.update_supply(db,request.supplierDetail)

    print('*******  Loop for - check barcode Exists *********')    
    for item in request.itemList:
        item.doc_id = request.doc_id
        category = uc_categories.get_category_byId(db,item.group_id)
        print(f"** category: {category.group_emei}",f"bar_code:{item.bar_code}")
        
        if category.group_emei == "Y" :
            vitemall = uc_vitemall.getSingle(db, item.bar_code, item.cc_id)
            if vitemall != None:
                alert +=  f"Barcode '{vitemall.bar_code}' มีอยู่ที่ร้าน '{vitemall.wh_id}' จำนวน '{vitemall.qty}'"   
                continue     
        stockIn_d.append(uc_stockIn.add_stock_in_d(db,item))
        
    print("print stockIn_d")
    print(stockIn_d)
        
    print('*******  Loop for - insert item / stock detail *********')
    for item in stockIn_d:
        if item != None:
            item.doc_id = request.doc_id                        
            productM = uc_productM.getProductM(db, item)

            print(f">> bar_code:{item.bar_code}")

            if productM == None:
                item.pd_id = genidrandom.generate_id_random(db,"PRODUCT_ID", "P", 10000, "zero", request.cc_id)
                uc_productM.add_ProductM(db,item)                
            else:
                item.pd_id = productM.pd_id
                uc_productM.update_ProductM(db, item)
            

            print('**********************************')
            print('>> Checked product_unit ')            
            product_unit = uc_productUnit.get_productUnit_single(db,item.bar_code)

            if product_unit == None :
                print('>> add_ProductUnit')
                uc_productUnit.add_ProductUnit(db,item)
            else :
                print('>> ProductUnit Exists')

            uc_stockIn.update_stock_in_d(db,item)
            uc_stockCard.add_StockCard(db,item,request.vendor_id, request.vendor_name, request.wh_id)     

    uc_stockCard.execute_stored_procedure_mssql(db, 'app_Update_StockcardBF', request.doc_id, request.wh_id)
    
    if alert:
        return apiResponse.response(200,status="alert",message=alert)
    
    return apiResponse.response(200, status="success", message="")


@router.get("/stock_in/header")
async def get_StockHeader(doc_id:str ,cc_id:str
                , db: Session = Depends(get_db))-> stockIn.StockInHead:
    
    log.info('router-Model -> read_model')
    model = uc_stockIn.get_stock_in_h(db, doc_id,cc_id)
    return model


@router.get("/stock_in/detail")
async def get_StockDetail(doc_id:str,cc_id:str
                , db: Session = Depends(get_db))-> List[stockIn.vStockInDetail]:
    
    log.info('router-Model -> read_model')
    model = uc_stockIn.get_stock_in_d(db, doc_id,cc_id)
    return model
