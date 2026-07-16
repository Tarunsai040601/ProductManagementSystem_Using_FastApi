from sqlalchemy import Column, Integer, String, Boolean
from src.Utils.db import Base

class TaskModel(Base):
    __tablename__ = "username"
    __table_args__ = {"schema": "ProjectSchema"}

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)