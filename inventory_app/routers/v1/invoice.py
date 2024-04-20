import logging
import configparser
from sqlalchemy.exc import IntegrityError

import json

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException,Response
from fastapi import APIRouter
from bahttext import bahttext
# from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import  vItemAll as uc_vitemall , stockCard as uc_stockCard,invoice as uc_inv , current_datetime as cdate , warehouses as wh ,user
from ...dtos import Invoice,stockCard
from ...loggings import log
from ...utility import genidrandom , apiResponse
from ...entity import stockCard as et_stockcard,invoiceDetail,invoiceHeader


router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sales/add")
def invoice_save(request: Invoice.SaleHeaderRequest,
                      db: Session = Depends(get_db)):
    alert = "" 
    status = "success"
    
    try :    
        print(">> Function : invoice_save")
        print('>> generate_id_random - StockIn ')
        request.doc_id = genidrandom.generate_id_random(db,"Invoice", "IV", 100000, "yearmonth", request.cc_id)    

        print('************************************************')
        print('>> doc_id =',request.doc_id)
        print('************************************************')
        
        print('>> get_current_datetime ')
        curr_date,curr_datetime = cdate.get_current_datetime(db)
        lastDateTime = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")

        print('>> Add SaleHeader ')
        bath_txt     =  bahttext(float( request.total))
        bath_txt_vat =  bahttext(float( request.TotalBeforeTax))
        #uc_inv.saleHeaer_add(db,request,curr_datetime)
        SaleHeaderData = invoiceHeader.tbInvoiceHeader(
            doc_id= request.doc_id,
            doc_date= request.doc_date,
            wh_id= request.wh_id,    
            cust_id= request.customerDetail.cust_id,    
            cust_name= request.customerDetail.cust_fname,    
            cust_addr1= request.customerDetail.cust_addr1,    
            cust_addr2= request.customerDetail.cust_addr2,
            cust_tel= request.customerDetail.cust_tel,
            tax_id= request.customerDetail.tax_id,
            GrandTotal= request.GrandTotal,
            discount= request.discount,
            discount_pers= request.discount_pers,
            discount_cash= request.discount_cash,
            TotalBeforeTax= request.TotalBeforeTax,
            total= request.total,
            cash_return= request.cash_return,
            cash_receive= request.cash_receive,
            bath_txt= bath_txt,
            bath_txt_vat= bath_txt_vat,
            PRINT_VAT_TYPE= request.PRINT_VAT_TYPE,
            UEDIT= request.user_id,
            DEDIT= lastDateTime,
            cc_id = request.cc_id,
            doc_type = request.doc_type,
            chk_pay = request.chk_pay,
            pay_type = request.pay_type,
            )
        db.add(SaleHeaderData)
        
        for item in request.itemList:
            print('*************************')
            print('>> Add SaleDetail/Item List barcode :',item.bar_code)
            # uc_inv.SaleDetail_add(db,request.doc_id,item,curr_datetime)

            SaleDetailData = invoiceDetail.tbInvoiceDetail(
                    doc_id    = request.doc_id,
                    bar_code  = item.bar_code,
                    pd_name   = item.pd_name,
                    cost      = item.cost,
                    price     = item.price,
                    qty       = item.qty,
                    unit_id   = "1",
                    UEDIT     = item.UEDIT,
                    DEDIT     = lastDateTime,
                    cc_id     = item.cc_id,            
                    )
                    
            print('>> Add Stockcard barcode XXX :',item.bar_code)

            # sql_text = "Update tbstockcardBF set qty=qty+(-"+str(item.qty)+") where bar_code='"+item.bar_code+"'  and wh_id='"+item.wh_id+"' and cc_id='"+item.cc_id+"' and zyear=2024 "
            itemStockCard = et_stockcard.TbStockCard(                                                                               
                                bar_code = item.bar_code  
                                ,doc_id = request.doc_id                            
                                ,doc_date = request.doc_date 
                                ,date_in = lastDateTime
                                ,type_doc = "IV"
                                ,wh_id = request.wh_id
                                ,unit_id = 1
                                ,qty = item.qty
                                ,cost = item.cost
                                ,price = item.price
                                ,lot_no = ""
                                ,vd_cu_code = request.customerDetail.cust_id
                                ,vd_cu_name = request.customerDetail.cust_fname                          
                                ,cc_id = request.cc_id
                                )
            # result = uc_stockCard.add_StockCard(db,new_StockCard)          
        
            db.add(SaleDetailData)              
            db.add(itemStockCard)             
 
        db.commit()

        for item in request.itemList:
            uc_stockCard.execute_stockcardBF(db,request.wh_id,item.bar_code,item.qty,request.cc_id)            

    except IntegrityError as e:
        db.rollback()  
        alert = e
        status = "alert"
        print(f">>> Error updating record: {e}")
    finally:
        db.close()   
        return apiResponse.response(200, status=status, message=alert)


@router.get("/sales/print")
def invoice_print( doc_id:str,cc_id:str,
                   db: Session = Depends(get_db)) :
    
    log.info("router-warehouses -> create_warehouse")
      
    # doc_id = 'A01-IV2201100171'

    db_invH = uc_inv.get_SaleHeader(db, doc_id=doc_id)    
    db_invD = uc_inv.get_SaleDetail(db, doc_id=doc_id)    
    db_wh = wh.get_warehouse_singleById(db, wh_id=db_invH.wh_id) 
    db_user = user.get_singleById(db,db_invH.UEDIT)
    # _result_inv = json.dumps(db_inv, ensure_ascii=False, encoding='utf8')

    if (db_invH.pay_type=="CASH") :  
        db_invH.pay_type = "เงินสด"
    elif (db_invH.pay_type=="TRANS") :  
        db_invH.pay_type = "โอนเงิน/พร้อมเพย์"
    elif (db_invH.pay_type=="CREDIT") :  
        db_invH.pay_type = "บัตรเครดิต"

    curr_date,curr_datetime = cdate.get_current_datetime(db)
    lastDateTime = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
   #  return Response( _result_inv, media_type='application/json')
    return { 
             'warehouse': {db_wh} ,
             'user' : {db_user} ,
             'saleHeader' : {db_invH},
             'saleDetail' : db_invD,
             'current_date':lastDateTime,
             }
