import logging
import configparser

from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

# from ... import crud,schemas
from ...database import SessionLocal
from ...utility import genidrandom

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/generate_id")
async def generate_id(type_id:str,form:str,format:int,type_form:str,cc_id:str=None,
                      db: Session = Depends(get_db)):
  """
  API endpoint to generate random ID.
  """
  # Extract parameters from request body


  doc_id = genidrandom.generate_id_random(db,type_id, form, format, type_form, cc_id)

  # Return generated ID in JSON format
  return {"doc_id": doc_id}
  