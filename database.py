from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://pos_realme:Ca1u7p@5@mssql-2012.chaiyohosting.com:1433/srakraisoft_pos_realme"  
    "?driver=ODBC+Driver+17+for+SQL+Server"  
)


# SQLALCHEMY_DATABASE_URL = (
#     "mssql+pyodbc://sa:Adm1234@localhost:1433/POSDB_SHOP_MAY01"  
#     "?driver=ODBC+Driver+17+for+SQL+Server"  
# )



engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},  # only needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
