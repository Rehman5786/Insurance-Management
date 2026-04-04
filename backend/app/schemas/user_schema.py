from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    city: str
    platform: str
    weekly_income: int
    working_hours: int