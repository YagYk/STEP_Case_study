from app import models, schemas, mappers, database
from datetime import datetime

async def create_clinic(clinic: schemas.ClinicCreate):
    db_clinic = mappers.clinic_create_to_model(clinic)
    clinic_dict = db_clinic.dict(by_alias=True)
    result = await database.clinics_collection.insert_one(clinic_dict)
    clinic_dict["_id"] = result.inserted_id
    return clinic_dict

async def get_clinics(skip: int = 0, limit: int = 10):
    cursor = database.clinics_collection.find().skip(skip).limit(limit)
    clinics = await cursor.to_list(length=limit)
    return clinics 