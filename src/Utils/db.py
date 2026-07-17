from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.Utils.settings import settings

Base = declarative_base()
engine = create_engine(url=settings.DATABASECONNECT)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
