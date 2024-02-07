from typing import List

from fastapi import Depends, FastAPI, HTTPException
# from . import models,schemas
from sqlalchemy.orm import Session

# from .backup import schemas

from .database import SessionLocal, engine , Base
from .routers.v1 import warehouses,brands,vstockcards,categories 
from .use_cases import warehouses as ucwh
from .dtos import warehouses as dtos

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)



app = FastAPI()

# ********* START - CORS **************************** 
# แก้ไขปัญหา : blocked by CORS policy: No 'Access-Control-Allow-Origin'

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ********* END - CORS **************************** 

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# app.include_router(brands.router, prefix="/v1", tags=["brands"])
# app.include_router(warehouses.router, prefix="/v1", tags=["warehouse"])

app.include_router(brands.router, prefix="/v1", tags=["new"])
app.include_router(warehouses.router, prefix="/v1", tags=["new"])
app.include_router(vstockcards.router, prefix="/v1", tags=["new"])
app.include_router(categories.router, prefix="/v1", tags=["new"])

 