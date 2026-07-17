from sqlalchemy import Column, Integer, String, Boolean
from src.Utils.db import Base

class TaskModel(Base):
    __tablename__ = "username"
    __table_args__ = {"schema": "ProjectSchema"}

    id = Column(Integer, primary_key=True)
    ProductTitle = Column(String, nullable=False)
    description = Column(String, nullable=False)
    Price=Column(String)
    Comments=Column(String)