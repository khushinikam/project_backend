import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

# DB_USER = os.getenv("DB_USER")
# print(DB_USER)
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# print(DB_PASSWORD)
# DB_HOST = os.getenv("DB_HOST")
# print(DB_HOST)
# DB_NAME = os.getenv("DB_NAME")
# print(DB_NAME)
# DB_PORT = os.getenv("DB_PORT")
# print(DB_PORT)

print ("step 1")
# DATABASE_URL = "postgresql://postgres:root@db:5432/auth_db"
# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print ("Database creation started")
# print(DATABASE_URL)

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    connection.close()
    print("Postgres working")
        

except Exception as e:
    print("Postgres connection not successful",e)


sessionLocal = sessionmaker(
    bind = engine
)
print("Database step 3")
BaseClass = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally: 
        db.close()



        