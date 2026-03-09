from fastapi import FastAPI
from app.routers import shipments

app = FastAPI()

app.include_router(shipments.router)


@app.get("/")
def root():
    return {"message": "Smart Shipment Manager API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}