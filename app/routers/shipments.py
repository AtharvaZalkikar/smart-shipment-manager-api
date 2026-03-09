from fastapi import APIRouter
from app.schemas.shipment import ShipmentCreate, ShipmentResponse

router = APIRouter(
    prefix="/shipments",                            #Now the router automatically prefixes all endpoints with: /shipments
    tags=["Shipments"]
)

shipments = []


@router.get("/")
def get_shipments():
    return shipments


@router.post("/", response_model=ShipmentResponse)
def create_shipment(shipment: ShipmentCreate):

    shipment_id = len(shipments) + 1

    shipment_data = shipment.model_dump()
    shipment_data["id"] = shipment_id

    shipments.append(shipment_data)

    return shipment_data


@router.get("/{shipment_id}")
def get_shipment(shipment_id: int):

    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return shipment

    return {"error": "Shipment not found"}


@router.delete("/{shipment_id}")
def delete_shipment(shipment_id: int):

    for shipment in shipments:
        if shipment["id"] == shipment_id:
            shipments.remove(shipment)
            return {"message": "Shipment deleted"}

    return {"error": "Shipment not found"}