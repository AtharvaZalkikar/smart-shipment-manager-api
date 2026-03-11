from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import shipments

from sqlmodel import SQLModel
from app.database.db import engine
from app.models.shipment import Shipment

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    create_db_and_tables()
    yield
    # Shutdown logic (not needed yet)

'''
FastAPI starts
      ↓
lifespan() runs
      ↓
create_db_and_tables()
      ↓
SQLModel creates shipments table
      ↓
API ready
'''

app = FastAPI(lifespan=lifespan)

app.include_router(shipments.router, prefix="/api/v1")             #Useful for API versioning and cleaner endpoints

@app.get("/")
def root():
    return {"message": "Smart Shipment Manager API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}