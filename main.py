from fastapi import FastAPI
from src.Utils.db import Base,engine

Base.metadata.create_all(engine)
app=FastAPI()