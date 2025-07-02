# CMD Telehealth Platform (Levels 1-3)

A FastAPI backend for managing clinics and their services using MongoDB.

## Features
- Add a new clinic (POST /clinics)
- Layered architecture (models, DTOs, mappers, controllers)
- MongoDB database

## Prerequisites
- MongoDB server running on localhost:27017
- Python 3.7+

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## MongoDB Setup
Make sure MongoDB is running on your system. If you're using MongoDB Atlas or a different connection string, update the `MONGODB_URL` in `app/database.py`.

## API Endpoints
- POST /clinics/ - Add a new clinic
- GET /clinics/ - Get all clinics
- Swagger UI: http://127.0.0.1:8000/docs 