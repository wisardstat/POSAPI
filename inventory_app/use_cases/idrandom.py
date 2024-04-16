from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy import  and_ 
from ..entity import idrandom as et_idrandom
from sqlalchemy.exc import IntegrityError


def get_listidrandom(db: Session, crtid: str ,frm: str, chk_cc_id:int, cc_id:str):
    print("get_listidrandom")

    # Build the filter criteria
    
    criteria = and_(
                    et_idrandom.TbIdRandom.CrtID == crtid,
                    et_idrandom.TbIdRandom.Frm == frm,
                    et_idrandom.TbIdRandom.cc_id == cc_id if chk_cc_id == 1 else True
                    )
    print("criteria=>",criteria)
    result = (
        db.query(et_idrandom.TbIdRandom)
        .filter(criteria)
        .all()
    )
    return result


def get_IDNum(db: Session, crtid: str ,frm: str, chk_cc_id:int, cc_id:str):
    
    print("get_IDNum")

    # Build the filter criteria
    
    criteria = and_(
                    et_idrandom.TbIdRandom.CrtID == crtid,
                    et_idrandom.TbIdRandom.Frm == frm,
                    et_idrandom.TbIdRandom.cc_id == cc_id if chk_cc_id == 1 else True
                    )


    print("criteria=>",criteria)
    result = (
                db.query(et_idrandom.TbIdRandom)
                .filter(criteria)
                .first()
             )
    print(result)
    if result==None :
        return 0
    else :
        return int(result.IDNum)

def create_idrandom(db: Session, crtid: str ,frm: str, type_doc:str, id_num:str,cc_id:str):
    print("create_idrandom",)
    db_idrandom = et_idrandom.TbIdRandom(
                            CrtID = crtid,
                            Frm = frm,
                            TypeDoc = type_doc,
                            IDNum = id_num,
                            cc_id=cc_id if cc_id else None 
                            )
    db.add(db_idrandom)
    db.commit()
    # db.refresh(db_idrandom)
    return db_idrandom




def update_IDNum(db: Session, crtid: str, cc_id: str, new_id_num: str):
    try:
        criteria = and_(
            et_idrandom.TbIdRandom.CrtID == crtid,
            et_idrandom.TbIdRandom.cc_id == cc_id if cc_id else True
        )

        result = (
            db.query(et_idrandom.TbIdRandom)
            .filter(criteria)
            .update(values={"IDNum": new_id_num})
        )        

        if result:            
            db.commit()
            return True  # Update successful

    except IntegrityError as e:
        # Handle potential database constraint violation (optional)
        db.rollback()  # Rollback the transaction on error
        print(f"Error updating record: {e}")
        return False

    # finally:
    #     db.close()  # Always close the session