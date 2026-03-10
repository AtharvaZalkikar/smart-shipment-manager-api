from fastapi import APIRouter
from app.schemas.shipment import ShipmentCreate, ShipmentResponse
from app.services import shipment_service
from fastapi import HTTPException

from sqlmodel import Session, select
from fastapi import Depends
from app.database.db import get_session
from app.models.shipment import Shipment

router = APIRouter(
    prefix="/shipments",                            #Now the router automatically prefixes all endpoints with: /shipments
    tags=["Shipments"]
)

@router.get("/", response_model=list[ShipmentResponse])
def get_shipments(
    limit: int = 10,
    offset: int = 0,
    sort_by: str = "id",
    order: str = "asc",
    status: str | None = None,
    destination: str | None = None,
    session: Session = Depends(get_session)
):

    return shipment_service.get_shipments(
        session,
        limit,
        offset,
        sort_by,
        order,
        status,
        destination
    )

@router.post("/", response_model=ShipmentResponse)
def create_shipment(shipment: ShipmentCreate, session: Session = Depends(get_session)):

    db_shipment = shipment_service.create_shipment(
        session,
        shipment.model_dump()
    )

    return db_shipment

@router.get("/{shipment_id}", response_model=ShipmentResponse)
def get_shipment(
    shipment_id: int,
    session: Session = Depends(get_session)
):

    shipment = shipment_service.get_shipment(session, shipment_id)

    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")

    return shipment


@router.delete("/{shipment_id}")
def delete_shipment(
    shipment_id: int,
    session: Session = Depends(get_session)
):

    shipment = shipment_service.delete_shipment(session, shipment_id)

    if not shipment:
        raise HTTPException( status_code=404, detail="Shipment not found")

    return {"message": "Shipment deleted"}