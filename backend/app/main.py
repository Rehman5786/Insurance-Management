from fastapi import FastAPI
from app.routes import user_routes

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Parametric Insurance API Running 🚀"}

app.include_router(user_routes.router)

from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)