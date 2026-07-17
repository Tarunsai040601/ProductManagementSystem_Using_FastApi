from sqlalchemy import Column,Integer,String,Boolean
from src.Utils.db import Base

class UserModel(Base):
    __tablename__="userRegister"
    __table_args__={"schema":"ProjectSchema"}
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)