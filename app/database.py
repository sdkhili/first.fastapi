from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictRow
import time
from .config import settings

#SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    with engine.connect() as connection:
        print("Successfully connected to the database")
except Exception as error:
    print(f"Error connecting to the database: {error}")
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# while True:
    
#     try:
#         conn = psycopg2.connect(host='localhost', 
#                                 database='fastapi', 
#                                 user='postgres', 
#                                 password='root', 
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Succesfully connected the DB")
#         break
#     except Exception as error:
#         print("Failed to connect the DB")
#         print("Error: ", error)    
#         time.sleep(2)