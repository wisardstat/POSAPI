from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import  and_ 
from ..entity import productUnit as ent
from ..dtos import stockIn 


def add_ProductUnit(db: Session, item: stockIn.StockItem):            
    try:
        print("add_ProductUnit")
        new_ProductUnit = ent.TbProductUnit(                                                   
                            pd_id = item.pd_id
                            ,bar_code = item.bar_code  
                            ,price1 = item.cost  
                            ,price2 = item.cost  
                            ,price3 = item.cost 
                            ,last_cost = item.cost 
                            ,unit_id = 1
                            ,ratio = 1
                            ,cc_id =item.cc_id)
        
        db.add(new_ProductUnit)
        db.commit()
        if new_ProductUnit:
            print("Data inserted successfully (TbProductUnit)!")               
            return new_ProductUnit 

    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
    finally:
        db.close() 