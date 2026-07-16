from fastapi import FastAPI
from src.Utils.db import Base,engine
from src.Tasks.Models import TaskModel
Base.metadata.create_all(engine)
app=FastAPI()