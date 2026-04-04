from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base

class RiskProfile(Base):
    __tablename__ = "risk_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    risk_score = Column(Float)
    expected_loss_percent = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())