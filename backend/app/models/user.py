from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    phone = Column(String(15))
    city = Column(String(50))
    platform = Column(String(50))
    weekly_income = Column(Integer)
    working_hours = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())