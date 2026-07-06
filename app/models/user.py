from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    name = Column(String)
    score = Column(Integer, default=0)
    exams_taken = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
