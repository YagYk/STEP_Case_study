from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# MongoDB connection string - you can change this to your MongoDB instance
MONGODB_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "cmd_telehealth"

# Async client for FastAPI
async_client = AsyncIOMotorClient(MONGODB_URL)
database = async_client[DATABASE_NAME]

# Collections
clinics_collection = database.clinics
services_collection = database.services

# Sync client for initialization (if needed)
sync_client = MongoClient(MONGODB_URL)
sync_database = sync_client[DATABASE_NAME]

def init_db():
    """Initialize database indexes"""
    # Create indexes for better performance
    clinics_collection.create_index("clinic_id", unique=True)
    services_collection.create_index("service_id") 