from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import  and_ ,or_ , func
from ..dtos import Invoice 
from datetime import datetime, timedelta,date

from ..entity import invoiceHeader as enh,invoiceDetail
from bahttext import bahttext

def saleHeaer_add(db: Session
                  ,request: Invoice.SaleHeaderRequest
                  ,curr_datetime:datetime):
    
    print(">>> Function : saleHeaer_add") 
    
    
    lastDateTime = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
    doc_date = curr_datetime.strftime("%Y-%m-%d")

    bath_txt     =  bahttext(float( request.total))
    bath_txt_vat =  bahttext(float( request.TotalBeforeTax))
    
    SaleHeaderData = enh.tbInvoiceHeader(
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
    db.commit()
    db.refresh(SaleHeaderData)

    if SaleHeaderData:
        print(">>> Data inserted >> TbInvoice_H << successfully!!")
        return SaleHeaderData 


def SaleDetail_add(db: Session
                   , doc_id:str
                   , item: Invoice.SaleDetailRequest
                   , curr_datetime:datetime
                   ) :

    lastDateTime = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")

    SaleDetailData = invoiceDetail.tbInvoiceDetail(
            doc_id    = doc_id,
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
    db.add(SaleDetailData)
    db.commit()
    # db.refresh(SaleDetailData)

    if SaleDetailData:
        print(">>> Data inserted >> TbInvoice_D << successfully!!")
        return SaleDetailData     


def get_SaleHeader(db: Session, doc_id:str, cc_id:str) :
    return ( db.query(enh.vInvoiceHeader)
             .filter( and_ (enh.vInvoiceHeader.doc_id == doc_id
                     ,enh.vInvoiceHeader.cc_id == cc_id))
             .first() )

def get_SaleDetail(db: Session, doc_id:str, cc_id:str) :
    return ( db.query(invoiceDetail.vInvoiceDetail)
             .filter( and_( invoiceDetail.vInvoiceDetail.doc_id == doc_id
                     ,invoiceDetail.vInvoiceDetail.cc_id == cc_id) )
             .all() )

def get_SaleByOfficer(db: Session ,wh_id:str, doc_date_st:date,doc_date_en:date, cc_id:str) :
    
    return ( db.query(
                         enh.vInvoiceHeader.UEDIT.label("user_id")
                        ,enh.vInvoiceHeader.USER_NAME.label("offier_name")
                        ,func.sum(enh.vInvoiceHeader.total).label("grand_total")
                      )
             .filter(
                        and_(
                                enh.vInvoiceHeader.doc_date >= doc_date_st,
                                enh.vInvoiceHeader.doc_date <= doc_date_en,
                                enh.vInvoiceHeader.cc_id == cc_id,
                                enh.vInvoiceHeader.wh_id == wh_id
                                )
                      )
             .group_by(
                 enh.vInvoiceHeader.UEDIT.label("user_id")
                 , enh.vInvoiceHeader.USER_NAME
             )
             .all() 
             
             )
