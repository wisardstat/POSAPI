from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter

# from ... import crud,schemas
from ...database import SessionLocal, engine
from ...use_cases import v_stockDailys as usecase
from ...dtos import v_stockDailys as dtos
from ...loggings import log

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/stockDailys/")
async def getListAll(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
) -> List[dtos.v_stockDailys_all]:

    log.info("router-stockDailys -> getListAll")

    vstockcard = usecase.getListAll(db, skip=skip, limit=limit)
    return vstockcard


@router.get("/stockDailys/GroupByBrand")
async def getListGroupByBrand(
    wh_id: str = "",
    categoty_id: str = "",
    brand_id: str = "",
    type_rp: str = "",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> List[dtos.v_stockDailyGroupByBrand]:

    log.info("router-stockDailys -> GroupByBrand")
    log.info("router-stockDailys -> brand_id =" + str(brand_id))
    log.info("router-stockDailys -> categoty_id =" + str(categoty_id))
    log.info("router-stockDailys -> wh_id =" + str(wh_id))
    log.info("router-stockDailys -> type_rp =" + str(type_rp))
    log.info("router-stockDailys -> skip =" + str(skip))
    log.info("router-stockDailys -> limit =" + str(limit))

    vstockcard = usecase.getListGroupByBrand(
        db,
        wh_id=wh_id,
        categoty_id=categoty_id,
        brand_id=brand_id,
        type_rp=type_rp,
        skip=skip,
        limit=limit,
    )
    return vstockcard


@router.get("/stockDailys/GroupByModel")
async def getListGroupByModel(
    wh_id: str = "",
    categoty_id: str = "",
    brand_id: str = "",
    type_rp: str = "",
    stock_date: str = "",
    find_pdname: str = "",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> List[dtos.v_stockDailyGroupByModel]:

    log.info("router-stockDailys -> GroupByModel")
    log.info("router-stockDailys -> brand_id =" + str(brand_id))
    log.info("router-stockDailys -> categoty_id =" + str(categoty_id))
    log.info("router-stockDailys -> wh_id =" + str(wh_id))
    log.info("router-stockDailys -> type_rp =" + str(type_rp))
    log.info("router-stockDailys -> stock_date =" + str(stock_date))
    log.info("router-stockDailys -> skip =" + str(skip))
    log.info("router-stockDailys -> limit =" + str(limit))

    print("router-stockDailys -> stock_date =", stock_date)

    vstockcard = usecase.getListGroupByModel(
        db,
        wh_id=wh_id,
        categoty_id=categoty_id,
        brand_id=brand_id,
        type_rp=type_rp,
        stock_date=stock_date,
        find_pdname =find_pdname,
        skip=skip,
        limit=limit,
    )
    return vstockcard


@router.get("/stockDailys/GroupByItem")
async def getListGroupByItem(
    wh_id: str = "",
    categoty_id: str = "",
    brand_id: str = "",
    model_name: str = "",
    type_rp: str = "",
    stock_date: str = "",
    find_pdname: str = "",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> List[dtos.v_stockDailyGroupByItem]:

    log.info("router-stockDailys -> +++++++++++++++++++")
    log.info("router-stockDailys -> getListGroupByItem")
    log.info("router-stockDailys -> brand_id =" + str(brand_id))
    log.info("router-stockDailys -> categoty_id =" + str(categoty_id))
    log.info("router-stockDailys -> wh_id =" + str(wh_id))
    log.info("router-stockDailys -> type_rp =" + str(type_rp))
    log.info("router-stockDailys -> stock_date =" + str(stock_date))
    log.info("router-stockDailys -> skip =" + str(skip))
    log.info("router-stockDailys -> limit =" + str(limit))

    print("router-stockDailys -> stock_date =", stock_date)

    vstockcard = usecase.getListGroupByItem(
        db,
        wh_id=wh_id,
        categoty_id=categoty_id,
        brand_id=brand_id,
        model_name=model_name,
        type_rp=type_rp,
        stock_date=stock_date,
        find_pdname=find_pdname,
        skip=skip,
        limit=limit,
    )
    return vstockcard


@router.get("/stockDailys/GroupByItem_totalQty")
async def getListGroupByItem_totalQty(
    wh_id: str = "",
    categoty_id: str = "",
    brand_id: str = "",
    model_name: str = "",
    type_rp: str = "",
    stock_date: str = "",
    find_pdname: str = "",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> dtos.v_stockDaily_totalQty:

    log.info("router-stockDailys -> +++++++++++++++++++")
    log.info("router-stockDailys -> getListGroupByItem")
    log.info("router-stockDailys -> brand_id =" + str(brand_id))
    log.info("router-stockDailys -> categoty_id =" + str(categoty_id))
    log.info("router-stockDailys -> wh_id =" + str(wh_id))
    log.info("router-stockDailys -> type_rp =" + str(type_rp))
    log.info("router-stockDailys -> stock_date =" + str(stock_date))
    log.info("router-stockDailys -> skip =" + str(skip))
    log.info("router-stockDailys -> limit =" + str(limit))

    print("router-stockDailys -> stock_date =", stock_date)

    vstockcard = usecase.getListGroupByItem_totalQty(
        db,
        wh_id=wh_id,
        categoty_id=categoty_id,
        brand_id=brand_id,
        model_name=model_name,
        type_rp=type_rp,
        stock_date=stock_date,
        find_pdname=find_pdname,
        skip=skip,
        limit=limit,
    )
    return vstockcard
