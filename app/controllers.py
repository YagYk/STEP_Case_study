from fastapi import APIRouter, HTTPException
from typing import List
from app import schemas, crud

clinic_router = APIRouter()

@clinic_router.post("/", response_model=dict)
async def create_clinic(clinic: schemas.ClinicCreate):
    return await crud.create_clinic(clinic)

@clinic_router.get("/", response_model=List[dict])
async def read_clinics(skip: int = 0, limit: int = 10):
    return await crud.get_clinics(skip=skip, limit=limit) 