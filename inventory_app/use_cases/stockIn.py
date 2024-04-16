from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import  and_ 
from ..entity import stockInD , stockInH , tbSupply , vstockInD , vstockInH
from ..dtos import stockIn 
from datetime import datetime


def add_stockIn_h(db: Session,request: stockIn.StockInRequest):            
    try:
        now = datetime.now()
        date_now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        formatted_date = date_now.strftime("%Y-%m-%d %H:%M:%S")
        print("add_stockIn_h")

        # if (request.vendor_name==""):        
        #     request.vendor_name="ไม่ระบุ"
        
        new_stock_in_h = stockInH.TbStockInH(
            doc_id= request.doc_id,
            doc_date= formatted_date,
            wh_id= request.wh_id,
            vendor_id= request.vendor_id,
            vendor_name= request.vendor_name,
            vendor_addr1= request.vendor_addr1,
            vendor_addr2= request.vendor_addr2,
            cc_id = request.cc_id,
            type_doc = request.type_doc,
            DOC_STATUS = request.DOC_STATUS      
        )
        
        db.add(new_stock_in_h)
        db.commit()
        db.refresh(new_stock_in_h)
        if new_stock_in_h:
            print("Data inserted successfully (TbStockInH)!")               
            return new_stock_in_h 

    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
    finally:
        db.close() 
        
def add_supply(db: Session,request: stockIn.supplierDetail):
    try:
        print("add_supply")

        new_supply = tbSupply.TbSupply(
            supply_id = request.supply_id,
            supply_name = request.supply_name,
            supply_addr = request.supply_addr,
            supply_addr1 = request.supply_addr1,
            supply_addr2 = request.supply_addr2,
            supply_tel = request.supply_tel,
            supply_postcode = request.supply_postcode,
            supply_tax_id = request.supply_tax_id,
            user_id = request.user_id,
            user_date = request.user_date,
            user_contact = request.user_contact,
            cc_id = request.cc_id
        )
        
        db.add(new_supply)
        db.commit()
        db.refresh(new_supply)
        if new_supply:
            print("Data inserted successfully (TbSupply)!")
            return True 
    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
        return False
    finally:
        db.close()  
 
def update_supply(db: Session, request: stockIn.supplierDetail):
    try:
        print("update_supply")
        
        supply_to_update = db.query(tbSupply.TbSupply).filter_by(supply_id=request.supply_id).update(values={
            "supply_name" : request.supply_name,
            "supply_addr" : request.supply_addr,
            "supply_addr1" : request.supply_addr1,
            "supply_addr2" : request.supply_addr2,
            "supply_tel" : request.supply_tel,
            "supply_tax_id" : request.supply_tax_id,
            "supply_postcode" : request.supply_postcode,
            "user_id" : request.user_id,
            "user_date" : request.user_date,
            "user_contact" : request.user_contact,
            "cc_id" : request.cc_id})

        if supply_to_update:            
            db.commit()
            print(f"Supply '{request.supply_id}' updated successfully!")
            return True  
        else:
            print(f"Supply with ID '{request.supply_id}' not found.")

    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
        return False

    finally:
        db.close()  

def add_stock_in_d(db: Session, request: stockIn.StockItem):
    try:
        print("add_stock_in_d")

        new_stock_in_d = stockInD.TbStockInD(
            doc_id = request.doc_id,
            bar_code = request.bar_code,
            pd_id = request.pd_id,
            pd_name = request.pd_name,
            group_id = request.group_id,
            brand_id = request.brand_id,
            model_id = request.model_id,
            color = request.color,
            cost = request.cost,
            qty = request.qty,
            #unit_id = request.unit_id,
            #lot_no = request.lot_no,
            #qty_receive = request.qty_receive,
            #cost_receive = request.cost_receive,
            STATUS = request.STATUS,
            cc_id = request.cc_id
        )
        db.add(new_stock_in_d)
        db.commit()
        
        stock_in_item = stockIn.StockItem(
            doc_id=new_stock_in_d.doc_id,
            bar_code=new_stock_in_d.bar_code,
            pd_id = new_stock_in_d.pd_id,
            pd_name = new_stock_in_d.pd_name,
            group_id = new_stock_in_d.group_id,
            brand_id = new_stock_in_d.brand_id,
            model_id = new_stock_in_d.model_id,
            color = new_stock_in_d.color,
            cost = new_stock_in_d.cost,
            qty = new_stock_in_d.qty,
            STATUS = new_stock_in_d.STATUS,
            cc_id = new_stock_in_d.cc_id
        )  
        print("Data inserted successfully (TbStockInD)!")
        return stock_in_item
    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
    finally:
        db.close()  
              
def update_stock_in_d(db: Session, item: stockIn.StockItem):
    try:
        print("update_stock_in_d")
        result = (
            db.query(stockInD.TbStockInD)
            .filter_by(bar_code = item.bar_code)
            .update(values={"pd_id" : item.pd_id})
        )

        if result:            
            db.commit()
            print("Data updated successfully (TbStockInD)!")
            return True

    except IntegrityError as e:
        db.rollback()  
        print(f"Error updating record: {e}")
        return False

    finally:
        db.close() 


def get_stock_in_h(db: Session, _doc_id:str, _cc_id:str):
    result = (
                db.query(vstockInH.vstockInH)
                .filter( (vstockInH.vstockInH.doc_id == _doc_id) 
                        ,(vstockInH.vstockInH.cc_id == _cc_id) 
                           )
                .first()
                )
    
    return result

def get_stock_in_d(db: Session, _doc_id:str, _cc_id:str):
    result = (
                db.query(vstockInD.vStockInD)
                .filter( ( vstockInD.vStockInD.doc_id == _doc_id) 
                        ,( vstockInD.vStockInD.cc_id == _cc_id)
                            )
                .all()
                )
    
    return result