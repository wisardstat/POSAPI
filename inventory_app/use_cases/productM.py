from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import  and_ 
from ..entity import productM 
from ..dtos import stockIn 



def getProductM(db: Session, item: stockIn.StockItem):
    print("getProductM")
    return db.query(productM.TbProductM).filter(productM.TbProductM.group_id == item.group_id
                                           ,productM.TbProductM.brand_id == item.brand_id
                                           ,productM.TbProductM.color == item.color
                                           ,productM.TbProductM.model_id == item.model_id).first()


def update_ProductM(db: Session, item: stockIn.StockItem):
    try:
        print("update_ProductM")
        productM_to_update = db.query(productM.TbProductM).filter(productM.TbProductM.group_id == item.group_id
                                           ,productM.TbProductM.brand_id == item.brand_id
                                           ,productM.TbProductM.color == item.color
                                           ,productM.TbProductM.model_id == item.model_id).update(values={"cost" : item.cost})
        
        if productM_to_update:            
            db.commit()
            print("productM updated successfully!")
            return True  

    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
        return False

    finally:
        db.close()  

def add_ProductM(db: Session, item: stockIn.StockItem):            
    try:
        print("add_ProductM")
        
        new_ProductM = productM.TbProductM(group_id = item.group_id
                            ,brand_id = item.brand_id
                            ,color = item.color
                            ,model_id = item.model_id  
                            ,pd_id = item.pd_id  
                            ,pd_name = item.pd_name  
                            ,cost = item.cost  
                            ,cc_id = item.cc_id
                            ,point_buy = 1
                            ,warranty_mn = 12)
        
        db.add(new_ProductM)
        db.commit()
        db.refresh(new_ProductM)
        if new_ProductM:
            print("Data inserted successfully (TbProductM)!")               
            return new_ProductM 

    except IntegrityError as e:        
        db.rollback()  
        print(f"Error updating record: {e}")
    finally:
        db.close() 