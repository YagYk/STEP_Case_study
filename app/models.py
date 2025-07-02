from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Clinic(Base):
    __tablename__ = "clinics"
    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(String, unique=True, index=True)
    clinic_name = Column(String)
    business_name = Column(String)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zip_code = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    date_created = Column(DateTime, default=datetime.utcnow)
    services = relationship("Service", back_populates="clinic")

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(String)
    service_name = Column(String)
    service_code = Column(String)
    service_description = Column(String)
    average_price = Column(Float)
    is_active = Column(Boolean, default=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"))
    clinic = relationship("Clinic", back_populates="services") 