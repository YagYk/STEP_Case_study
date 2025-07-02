from fastapi import FastAPI
from app.controllers import clinic_router
from app.database import init_db

app = FastAPI()

app.include_router(clinic_router, prefix="/clinics", tags=["Clinics"])

init_db() 