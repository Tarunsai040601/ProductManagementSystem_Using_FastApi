# import the sqlalchemy from database
from sqlalchemy import create_engine

# sqlalchemy is orm qurey builter
from sqlalchemy.orm import declarative_base, sessionmaker

# here i taken the setting of the database
from src.Utils.settings import settings

# taken instance class for declarative_base()
Base = declarative_base()

# database connection url
engine = create_engine(url=settings.DATABASECONNECT)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
