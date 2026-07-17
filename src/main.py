from fastapi import FastAPI
from src.Users.Routers import user_router
from src.Tasks.Routers import TaskRouter
from src.Utils.db import Base, engine


# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(TaskRouter)





