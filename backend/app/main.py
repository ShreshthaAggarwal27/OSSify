from fastapi import FastAPI
from backend.app.api.v1.router import api_router
from backend.app.db.postgres import engine, Base

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "OEG running 🚀"}