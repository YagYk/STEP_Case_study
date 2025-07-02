from sqlalchemy.orm import Session
from app import models, schemas, mappers

def create_clinic(db: Session, clinic: schemas.ClinicCreate):
    db_clinic = mappers.clinic_create_to_model(clinic)
    db.add(db_clinic)
    db.commit()
    db.refresh(db_clinic)
    return db_clinic

def get_clinics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Clinic).offset(skip).limit(limit).all() 