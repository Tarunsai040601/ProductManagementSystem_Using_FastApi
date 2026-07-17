# data base connection from .env file
from pydantic_settings import BaseSettings,SettingsConfigDict

class settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
    DATABASECONNECT:str
    SECRET_KEY: str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

settings=settings()