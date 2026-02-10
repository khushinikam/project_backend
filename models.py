from sqlalchemy import Column, Integer, String
from database import BaseClass

class User(BaseClass):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String, unique=True,nullable=False)
    email = Column(String, unique=True,nullable=False)
    password = Column(String)
    age = Column(Integer, nullable=True)