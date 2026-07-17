from fastapi import FastAPI
from src.Utils.db import Base,engine
from src.Tasks.Routers import TaskRouter
from src.Users.Routers import userRouter
Base.metadata.create_all(engine)
app=FastAPI()
app.include_router(TaskRouter)   
app.include_router(userRouter)                                                                                        