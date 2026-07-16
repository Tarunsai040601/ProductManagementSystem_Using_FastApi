from fastapi import FastAPI
from src.Utils.db import Base,engine
from src.Tasks.Routers import TaskRouter
Base.metadata.create_all(engine)
app=FastAPI()
app.include_router(TaskRouter)                                                                                         