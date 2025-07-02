from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ServiceBase(BaseModel):
    service_id: str
    service_name: str
    service_code: str
    service_description: Optional[str] = None
    average_price: Optional[float] = None
    is_active: Optional[bool] = True

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int
    class Config:
        orm_mode = True

class ClinicBase(BaseModel):
    clinic_id: str
    clinic_name: str
    business_name: str
    street_address: str
    city: str
    state: str
    country: str
    zip_code: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    date_created: Optional[datetime] = None

class ClinicCreate(ClinicBase):
    services: List[ServiceCreate] = []

class Clinic(ClinicBase):
    id: int
    services: List[Service] = []
    class Config:
        orm_mode = True 