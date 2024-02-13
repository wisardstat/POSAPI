from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote 
import configparser
 
config = configparser.ConfigParser()
config.read('./inventory_app/config.ini')
user        = config['DEFAULT']['user']
password    = config['DEFAULT']['password']
server      = config['DEFAULT']['server']
port        = config['DEFAULT']['port']
database    = config['DEFAULT']['database']

SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://{0}:%s@{1}:{2}/{3}?driver=ODBC+Driver+17+for+SQL+Server&schema=dbo".format(user,server,port,database)%quote(password)   
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},  # only needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
