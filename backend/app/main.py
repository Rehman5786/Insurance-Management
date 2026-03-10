from fastapi import FastAPI

app = FastAPI(title="AI Parametric Insurance Platform")

@app.get("/")
def root():
    return {"message": "Insurance Management API Running"}