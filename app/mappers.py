from app.models import Clinic, Service
from app.schemas import ClinicCreate, ServiceCreate

def clinic_create_to_model(clinic: ClinicCreate) -> Clinic:
    db_clinic = Clinic(
        clinic_id=clinic.clinic_id,
        clinic_name=clinic.clinic_name,
        business_name=clinic.business_name,
        street_address=clinic.street_address,
        city=clinic.city,
        state=clinic.state,
        country=clinic.country,
        zip_code=clinic.zip_code,
        latitude=clinic.latitude,
        longitude=clinic.longitude
    )
    db_clinic.services = [service_create_to_model(s) for s in clinic.services]
    return db_clinic

def service_create_to_model(service: ServiceCreate) -> Service:
    return Service(
        service_id=service.service_id,
        service_name=service.service_name,
        service_code=service.service_code,
        service_description=service.service_description,
        average_price=service.average_price,
        is_active=service.is_active
    ) 