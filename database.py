from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_password = ""
db_user =""
db_endpoint = ""+"3306"
db_name = ""

database = "mysql+pymysql://"+db_user+":"+db_password+"@"+db_endpoint+"/"+db_name #connection a une base de donneés MySQL
engine = create_engine(database)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()