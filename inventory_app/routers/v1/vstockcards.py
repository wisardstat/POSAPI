
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
#from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import vstockcards as usecase , vItemAll as uc_vitemall , categories as uc_categories , warehouses as uc_wh 
from ...dtos import vstockcards as dtos
from ...loggings import  log
from ...utility import apiResponse

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vstockcard/barcode_exists")
async def get_BarcodeExists( bar_code: str="",
                             group_id: str="",
                             cc_id: str="",
                             db: Session = Depends(get_db)):
    
    log.info('router-vstockcard -> get_BarcodeExists')
    print('>> bar_code=',bar_code)
    print('>> group_id=',group_id)
    print('>> cc_id=',cc_id)

    category = uc_categories.get_category_byId(db,group_id)
    alert =""

    print(f">> category: {category.group_emei}",f"bar_code:{bar_code}")

    if category.group_emei == "Y" :
        vitemall = uc_vitemall.getSingle(db, bar_code, cc_id)

        if vitemall != None  :                     
            if vitemall.qty==0 :
                wh_name = uc_wh.get_warehouse_name(db,vitemall.wh_id)
                alert =  f"บาร์โค๊ด/Emei {vitemall.bar_code} เคยรับเข้าร้านแล้ว ล่าสุดอยู่ที่ร้าน {wh_name} "
                print(alert)                
            else :
                wh_name = uc_wh.get_warehouse_name(db,vitemall.wh_id)
                alert =  f"บาร์โค๊ด/Emei {vitemall.bar_code} มีอยู่ที่ร้าน {wh_name} จำนวน {vitemall.qty} ชิ้น"   
                print(alert)                
        else :
            alert = ""
    
    result = jsonable_encoder(alert)    
    return JSONResponse(content=result, media_type="application/json")

        
@router.get("/vstockcard/getVstockcardListAll")
async def getVstockcardListAll(skip: int = 0, limit: int = 10, db: Session = Depends(get_db))-> List[dtos.vstockcard]:

    log.info('router-vstockcard -> getVstockcardListAll')

    vstockcard = usecase.getListAll(db, skip=skip, limit=limit)
    return vstockcard

@router.get("/vstockcard/getListByDoc")
async def getListByDoc( 
                         doc_date_st:str=""
                        ,doc_date_en:str=""
                        ,wh_id:str = ""                                                
                        ,type_doc_id:str = ""    
                        ,find_cust_name:str = ""                                            
                        ,skip: int = 0, limit: int = 100
                        ,db: Session = Depends(get_db))-> List[dtos.vstockcard_getListByDoc]:
    
    log.info('router-vstockcard -> getListByDoc')        
    log.info('router-vstockcard -> wh_id ='+str(wh_id))
    log.info('router-vstockcard -> type_doc_id ='+str(type_doc_id))
    log.info('router-vstockcard -> skip ='+str(skip))
    log.info('router-vstockcard -> limit ='+str(limit))
    log.info('router-vstockcard -> doc_date ='+str(doc_date_st))

    vstockcard = usecase.getListByDoc(db
                                        , doc_date_st=doc_date_st
                                        , doc_date_en=doc_date_en
                                        , wh_id = wh_id
                                        , type_doc_id =type_doc_id 
                                        , find_cust_name =find_cust_name                                      
                                        , skip=skip
                                        , limit=limit)
    return vstockcard


@router.get("/vstockcard/getListByDoc_Total")
async def getListByDoc_Total( 
                         doc_date_st:str=""
                        ,doc_date_en:str=""
                        ,wh_id:str = ""                                                
                        ,type_doc_id:str = ""                        
                        ,find_cust_name:str = ""                        
                        ,skip: int = 0, limit: int = 100
                        ,db: Session = Depends(get_db))-> dtos.vstockcard_getListByDoc_Total:
    
    log.info('router-vstockcard -> getListByDoc_Total')        
    log.info('router-vstockcard -> wh_id ='+str(wh_id))
    log.info('router-vstockcard -> type_doc_id ='+str(type_doc_id))
    log.info('router-vstockcard -> skip ='+str(skip))
    log.info('router-vstockcard -> limit ='+str(limit))
    log.info('router-vstockcard -> doc_date_st ='+str(doc_date_st))
    log.info('router-vstockcard -> doc_date_en ='+str(doc_date_en))

    vstockcard = usecase.getListByDoc_Total(db
                                        , doc_date_st=doc_date_st
                                        , doc_date_en=doc_date_en
                                        , wh_id = wh_id
                                        , type_doc_id =type_doc_id
                                        , find_cust_name =find_cust_name
                                        , skip=skip
                                        , limit=limit)
    return vstockcard



@router.get("/vstockcard/getListByItem")
async def getListByItem( 
                         doc_date_st:str=""
                        ,doc_date_en:str=""
                        ,wh_id:str = ""                  
                        ,type_doc_id:str=""
                        ,group_id:str=""
                        ,brand_id:str=""
                        ,model_id:str=""
                        ,find_cust_name:str = ""                        
                        ,find_pd_name:str = ""                                            
                        ,skip: int = 0, limit: int = 100
                        ,db: Session = Depends(get_db))-> List[dtos.vstockcard_getListByItem]:
    
    log.info('router-vstockcard -> getListByItem +++++++++++++++++++++')        
    log.info('router-vstockcard -> wh_id ='+str(wh_id))
    log.info('router-vstockcard -> type_doc_id ='+str(type_doc_id))
    log.info('router-vstockcard -> group_id ='+str(group_id))
    log.info('router-vstockcard -> brand_id ='+str(brand_id))
    log.info('router-vstockcard -> model_id ='+str(model_id))
    log.info('router-vstockcard -> pd_name ='+str(find_pd_name))
    log.info('router-vstockcard -> skip ='+str(skip))
    log.info('router-vstockcard -> limit ='+str(limit))
    log.info('router-vstockcard -> doc_date ='+str(doc_date_st))

    vstockcard = usecase.getListByItem(db
                                        , doc_date_st=doc_date_st
                                        , doc_date_en=doc_date_en
                                        , wh_id = wh_id
                                        , type_doc_id =type_doc_id 

                                        , group_id =group_id 
                                        , brand_id =brand_id 
                                        , model_id =model_id                                                                                 

                                        , find_cust_name =find_cust_name                                      
                                        , find_pd_name =find_pd_name                                      
                                        , skip=skip
                                        , limit=limit)
    return vstockcard
        

@router.get("/vstockcard/getListByItem_Total")
async def getListByItem_Total( 
                         doc_date_st:str=""
                        ,doc_date_en:str=""
                        ,wh_id:str = ""                  
                        ,type_doc_id:str=""
                        ,group_id:str=""
                        ,brand_id:str=""
                        ,model_id:str=""
                        ,find_cust_name:str = ""                        
                        ,find_pd_name:str = ""                                            
                        ,skip: int = 0, limit: int = 100
                        ,db: Session = Depends(get_db))-> dtos.vstockcard_getListByItem_Total:
    
    log.info('router-vstockcard -> getListByItem +++++++++++++++++++++')        
    log.info('router-vstockcard -> wh_id ='+str(wh_id))
    log.info('router-vstockcard -> type_doc_id ='+str(type_doc_id))
    log.info('router-vstockcard -> group_id ='+str(group_id))
    log.info('router-vstockcard -> brand_id ='+str(brand_id))
    log.info('router-vstockcard -> model_id ='+str(model_id))
    log.info('router-vstockcard -> pd_name ='+str(find_pd_name))
    log.info('router-vstockcard -> skip ='+str(skip))
    log.info('router-vstockcard -> limit ='+str(limit))
    log.info('router-vstockcard -> doc_date ='+str(doc_date_st))

    vstockcard = usecase.getListByItem_Total(db
                                        , doc_date_st=doc_date_st
                                        , doc_date_en=doc_date_en
                                        , wh_id = wh_id
                                        , type_doc_id =type_doc_id 

                                        , group_id =group_id 
                                        , brand_id =brand_id 
                                        , model_id =model_id                                                                                 

                                        , find_cust_name =find_cust_name                                      
                                        , find_pd_name =find_pd_name                                      
                                        , skip=skip
                                        , limit=limit)
    return vstockcard        

@router.get("/vstockcard/history_search")
async def getHistorySearch(bar_code:str
                            ,cc_id:str
                            ,db: Session = Depends(get_db))-> List[dtos.vstockcard]:
                                                          
    vstockcard = usecase.getHistorySearch(db,bar_code,cc_id)

    return vstockcard      

    

