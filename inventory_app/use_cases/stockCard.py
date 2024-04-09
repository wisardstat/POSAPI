from sqlalchemy.orm import Session 
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

from ..entity import stockCard as ent
from ..dtos import stockIn 
from datetime import datetime

def execute_stored_procedure_mssql(db: Session, procedure_name, doc_id, wh_id): 

    try:
        print(">>> execute_stored_procedure_mssql")       

        sql_text = text(f"EXEC {procedure_name} 'SI', '{doc_id}', '{wh_id}' ")
        db.execute(sql_text)
        db.commit();

        print("sql =",sql_text)

    except IntegrityError as e: 

        db.rollback()  
        print(f">>> Error!! updating record: {e}")

    finally:
        db.close()  # Close the session after use

        
def add_StockCard(db: Session, item: stockIn.StockItem , vendor_id:str, vendor_name:str , wh_id:str):            
    try:
        print(">>> add_StockCard")
        now = datetime.now()
        date_now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        
        formatted_date_in = now.strftime("%Y-%m-%d %H:%M:%S")
        formatted_doc_date = date_now.strftime("%Y-%m-%d %H:%M:%S")
        
        new_StockCard = ent.TbStockCard(                                                   
                            _pd_id = item.pd_id
                            ,bar_code = item.bar_code  
                            ,doc_id = item.doc_id
                            ,cost = item.cost
                            ,doc_date = formatted_doc_date 
                            ,type_doc = 1 
                            ,wh_id = wh_id
                            ,unit_id = 1
                            ,qty = item.qty
                            ,price = item.cost
                            ,lot_no = item.lot_no
                            ,vd_cu_code = vendor_id
                            ,vd_cu_name = vendor_name
                            ,date_in = formatted_date_in
                            ,cc_id = item.cc_id)
        
        db.add(new_StockCard)
        db.commit()
        db.refresh(new_StockCard)
        if new_StockCard:
            print(">>> Data inserted successfully (TbStockCard)!")               
            return new_StockCard 

    except IntegrityError as e:        
        db.rollback()  
        print(f">>> Error updating record: {e}")
    finally:
        db.close() 
