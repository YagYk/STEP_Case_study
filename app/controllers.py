from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database

clinic_router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@clinic_router.post("/", response_model=schemas.Clinic)
def create_clinic(clinic: schemas.ClinicCreate, db: Session = Depends(get_db)):
    return crud.create_clinic(db, clinic)

@clinic_router.get("/", response_model=List[schemas.Clinic])
def read_clinics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_clinics(db, skip=skip, limit=limit) 