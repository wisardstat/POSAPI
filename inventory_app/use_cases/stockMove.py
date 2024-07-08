from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import  and_ 
from ..entity import tbStockMovD , tbStockMovH
from ..dtos import stockMove 
from datetime import datetime

def add_stockMov_d(db: Session,request: stockMove.ItemDetail):            
    try:
        now = datetime.now()
        date_now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        formatted_date = date_now.strftime("%Y-%m-%d %H:%M:%S")
        print("add_stockMov_d")
        
        new_stock_mov_d = tbStockMovD.TbStockMovD(
            wh_id = request.wh_id,
            doc_id = request.doc_id,
            bar_code = request.bar_code,
            pd_name = request.pd_name,
            group_id = request.group_id,
            brand_id = request.brand_id,
            model_id = request.model_id,
            color = request.color,
            cost = request.cost,
            Qty = request.qty,
            UEDIT = request.UEDIT,
            DEDIT = formatted_date,
            cc_id = request.cc_id,
        )
        
        db.add(new_stock_mov_d)
        db.commit()
        db.refresh(new_stock_mov_d)
        if new_stock_mov_d:
            print("Data inserted successfully (TbStockMovD)!")               
            return new_stock_mov_d 

    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
    finally:
        db.close() 
        
def add_stockMov_h(db: Session,request: stockMove.StockMoveRequest):            
    try:
        now = datetime.now()
        date_now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        formatted_date = date_now.strftime("%Y-%m-%d %H:%M:%S")
        print("add_stockMov_h")
        
        new_stock_mov_h = tbStockMovH.TbStockMovH(
               doc_id = request.doc_id,
               doc_date = request.doc_date,
                wh_from =  request.wh_from,
                wh_target = request.wh_target,
                comment =  request.comment,
                UEDIT = request.UEDIT,
                DEDIT = formatted_date,
                cc_id = request.cc_id
        )
        
        db.add(new_stock_mov_h)
        db.commit()
        db.refresh(new_stock_mov_h)
        if new_stock_mov_h:
            print("Data inserted successfully (TbStockMovH)!")               
            return new_stock_mov_h 

    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
    finally:
        db.close() 