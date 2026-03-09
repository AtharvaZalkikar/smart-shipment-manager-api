from fastapi import FastAPI
from app.routers import shipments

app = FastAPI()

app.include_router(shipments.router, prefix="/api/v1")             #Useful for API versioning and cleaner endpoints


@app.get("/")
def root():
    return {"message": "Smart Shipment Manager API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}