from fastapi import FastAPI
from pydantic import BaseModel #pydantic models

app = FastAPI()

shipments = [] #temporary storage/database

# ShipmentCreate → request schema
class ShipmentCreate(BaseModel):
    destination: str
    status: str

'''
What response_model Does:

1 Validate response data
2 Filter unwanted fields
3 Improve Swagger docs
4 Generate OpenAPI schema
'''
# ShipmentResponse → response schema
class ShipmentResponse(BaseModel):   #in production we want to control the response structure
    id: int
    destination: str
    status: str


@app.get("/")
def root():
    return {"message": "Smart Shipment Manager API is running"}

@app.get("/health")
def health_check():
    return {"status" : "healthy"}

@app.get("/shipments")
def get_shipments():
    return shipments

@app.get("/shipments/{shipment_id}")
def get_shipments(shipment_id: int):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return shipment
    return {"error": "Shipment not found"}

@app.post("/shipments", response_model=ShipmentResponse)
def create_shipment(shipment: ShipmentCreate):
    shipment_id = len(shipments) + 1

    shipment_data = shipment.model_dump()  # convert Pydantic → dict
    shipment["id"] = shipment_id

    shipments.append(shipment_data)
    return shipment_data   

@app.delete("/shipments/{shipment_id}")
def delete_shipment(shipment_id: int):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            shipments.remove(shipment)
            return {"message": "Shipment deleted"}
    return {"error": "Shipment not found"}