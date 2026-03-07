from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart Shipment Manager API is running"}

@app.get("/health")
def health_check():
    return {"status" : "healthy"}

shipments = [] #temporary storage/database

@app.get("/shipments")
def get_shipments():
    return shipments

@app.get("/shipments/{shipment_id}")
def get_shipments(shipment_id: int):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return shipment
    return {"error": "Shipment not found"}

@app.post("/shipments")
def create_shipment(shipment:dict):
    shipment_id = len(shipments) + 1
    shipment["id"] = shipment_id
    shipments.append(shipment)
    return shipment   

@app.delete("/shipments/{shipment_id}")
def delete_shipment(shipment_id: int):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            shipments.remove(shipment)
            return {"message": "Shipment deleted"}
    return {"error": "Shipment not found"}