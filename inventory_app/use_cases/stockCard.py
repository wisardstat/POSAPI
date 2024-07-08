from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

from ..entity import stockCard as ent
from ..dtos import stockIn, stockCard ,stockMove
from ..use_cases import current_datetime as cdate


from datetime import datetime


def execute_stored_procedure_mssql(db: Session, procedure_name, doc_id, wh_id):

    try:
        print(">>> Function : execute_stored_procedure_mssql")
        print(">>> execute_stored_procedure_mssql")

        sql_text = text(f"EXEC {procedure_name} 'SI', '{doc_id}', '{wh_id}' ")
        db.execute(sql_text)
        db.commit()

        print("sql =", sql_text)

    except IntegrityError as e:

        db.rollback()
        print(f">>> Error!! updating record: {e}")

    finally:
        db.close()  # Close the session after use


def add_StockCard(db: Session, itemStockCard: ent.TbStockCard):

    try:
        print(">>> Function : add_StockCard")

        curr_date, curr_datetime = cdate.get_current_datetime(db)

        formatted_date_in = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
        # formatted_doc_date = date_now.strftime("%Y-%m-%d %H:%M:%S")

        itemStockCard.date_in = formatted_date_in

        db.add(itemStockCard)
        db.commit()
        db.refresh(itemStockCard)
        if itemStockCard:
            print(">> Data inserted >> TbStockCard << successfully!!")
            return itemStockCard

    except IntegrityError as e:
        db.rollback()
        print(f">>> Error updating record: {e}")
    finally:
        db.close()

def add_StockMoveCard(db: Session, stockMove:stockMove.StockMoveRequest,stockMoveItem:stockMove.ItemDetail):

    try:
 
        print(">>> Function : add_StockMoveCard")
        curr_date, curr_datetime = cdate.get_current_datetime(db)
        formatted_date_in = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
        
        itemStockCard = ent.TbStockCard(      
        doc_id = stockMove.doc_id,
        doc_date = stockMove.doc_date,
        type_doc = stockMove.type_doc,
        bar_code = stockMoveItem.bar_code,
        cc_id = stockMove.cc_id,
        qty = stockMoveItem.qty,
        wh_id = stockMoveItem.wh_id,
        cost = stockMoveItem.cost,
        date_in = formatted_date_in
        )
        
        db.add(itemStockCard)
        db.commit()
        db.refresh(itemStockCard)
        if itemStockCard:
            print(">> Data inserted >> add_StockMoveCard << successfully!!")
            return itemStockCard

    except IntegrityError as e:
        db.rollback()
        print(f">>> Error updating record: {e}")
    finally:
        db.close()


def execute_stockcardBF(db: Session, wh_id: str, barcode: str, qty: int, cc_id: str):

    try:
        print(">>> Function : execute_stored_procedure_mssql")
        print(">>> execute_stored_procedure_mssql")

        sql_text = text(
            f"Update tbstockcardBF set qty=qty+(-{str(qty)}) where bar_code='{barcode}' and wh_id='{wh_id}' and cc_id='{cc_id}' and zyear=2024 "
        )
        print(sql_text)

        db.execute(sql_text)
        db.commit()

        print("sql =", sql_text)

    except IntegrityError as e:

        db.rollback()
        print(f">>> Error!! updating record: {e}")

    finally:
        db.close()  # Close the session after use


