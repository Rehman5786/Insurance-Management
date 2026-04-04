from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.models.risk_profile import RiskProfile
from app.ai.risk_model import calculate_risk

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        phone=user.phone,
        city=user.city,
        platform=user.platform,
        weekly_income=user.weekly_income,
        working_hours=user.working_hours
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 🔥 AI Risk Calculation
    risk_score, expected_loss = calculate_risk(user.city)

    risk = RiskProfile(
        user_id=new_user.id,
        risk_score=risk_score,
        expected_loss_percent=expected_loss
    )

    db.add(risk)
    db.commit()

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "risk_score": risk_score,
        "expected_loss_percent": expected_loss
    }