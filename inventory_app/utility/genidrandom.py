import datetime
from ..database import SessionLocal, engine
from ..use_cases import idrandom as uc_idrandom
from sqlalchemy.orm import Session


def generate_id_random(db: Session,type_id, form, format, type_form, cc_id):
    
    print(">> Function : generate_id_random")
    # Check if cc_id is empty string
    chk_cc_id = 1 if cc_id else 0

    # Update form based on type_form (yearmonth)
    if type_form == "yearmonth":
      form += str(datetime.datetime.now().strftime("%y%m"))[-4:]

    # Check existence of record in IDRandom table 
    # cnt_idrandom = len(uc_idrandom.get_listidrandom(db,type_id,form,chk_cc_id,cc_id))    
    last_id = uc_idrandom.get_IDNum(db, type_id, form, chk_cc_id, cc_id)        
    # New record creation logic
    # if cnt_idrandom == 0:
    if last_id == 0:
      if chk_cc_id == 0:
        new_id = 1
        # Insert new record without cc_id
        uc_idrandom.create_idrandom(db, type_id, form, "N", new_id, cc_id)
        if type_form == "zero":
          doc_id = f"{form}{str(format + new_id)[1:]}"
        else:
          doc_id = f"{form}{format + new_id}"
      else:
        new_id = 1
        # Insert new record with cc_id
        uc_idrandom.create_idrandom(db, type_id, form, "N", new_id, cc_id)
        if type_form == "zero":
          doc_id = f"{cc_id}-{form}{str(format + new_id)[1:]}"
        else:
          doc_id = f"{cc_id}-{form}{format + new_id}"
    else:
      # Existing record update logic
      if chk_cc_id == 0:
        # Update record without cc_id
        # last_id = uc_idrandom.get_IDNum(db, type_id, form, chk_cc_id, None)        
        if type_form == "zero":
          doc_id = f"{form}{str(format + last_id + 1)[1:]}"
        else:
          doc_id = f"{form}{format + last_id + 1}"
        uc_idrandom.update_IDNum(db, type_id, None, str(last_id + 1))
      else:
        # Update record with cc_id
        # last_id = uc_idrandom.get_IDNum(db, type_id, form, chk_cc_id, cc_id)        
        if type_form == "zero":
          doc_id = f"{cc_id}-{form}{str(format + last_id + 1)[1:]}"
        else:
          doc_id = f"{cc_id}-{form}{format + last_id + 1}"
        uc_idrandom.update_IDNum(db, type_id, cc_id, str(last_id + 1))
    return doc_id