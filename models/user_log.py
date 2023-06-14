from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserLog(Base):
    __tablename__ = "api_calls"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
