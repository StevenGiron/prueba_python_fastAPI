from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://developer:qS*7Pjs3v0kw@db.g97.io:5432/data_analyst"
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
