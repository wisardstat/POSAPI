# import logging
# import configparser

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine , Base
from .routers.v1 import warehouses,brands,vstockcards,categories,v_stockDailys,models ,type_doc,genidrandom, stockIn,user,supply,customer,product,invoice
from .use_cases import warehouses as ucwh
from .dtos import warehouses as dtos
from fastapi.middleware.cors import CORSMiddleware
from .loggings import  log

Base.metadata.create_all(bind=engine)

log.info('main - Reload')

app = FastAPI()

# ********* START - CORS **************************** 
# แก้ไขปัญหา : blocked by CORS policy: No 'Access-Control-Allow-Origin'
origins = [    
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",      
            
    "http://45.32.102.157:8080", 
    "http://45.32.102.157:4200", 
    'https://d420-2401-c080-1400-5950-c8f5-f8d-81ab-d65a.ngrok-free.app',
    "https://5637-2401-c080-1400-5950-c8f5-f8d-81ab-d65a.ngrok-free.app",

 

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

app.include_router(type_doc.router, prefix="/v1", tags=["new"])
app.include_router(brands.router, prefix="/v1", tags=["new"])
app.include_router(models.router, prefix="/v1", tags=["new"])
app.include_router(warehouses.router, prefix="/v1", tags=["new"])
app.include_router(vstockcards.router, prefix="/v1", tags=["new"])
app.include_router(categories.router, prefix="/v1", tags=["new"])
app.include_router(v_stockDailys.router, prefix="/v1", tags=["new"])
app.include_router(genidrandom.router, prefix="/v1", tags=["new"])
app.include_router(stockIn.router, prefix="/v1", tags=["new"])
app.include_router(user.router, prefix="/v1", tags=["new"])
app.include_router(supply.router, prefix="/v1", tags=["new"])
app.include_router(customer.router, prefix="/v1", tags=["new"])
app.include_router(product.router, prefix="/v1", tags=["new"])
app.include_router(invoice.router, prefix="/v1", tags=["new"])

 