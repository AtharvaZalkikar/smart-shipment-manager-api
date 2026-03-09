from fastapi import APIRouter
from app.schemas.shipment import ShipmentCreate, ShipmentResponse

from sqlmodel import Session, select
from fastapi import Depends
from app.database.db import get_session
from app.models.shipment import Shipment

router = APIRouter(
    prefix="/shipments",                            #Now the router automatically prefixes all endpoints with: /shipments
    tags=["Shipments"]
)


@router.get("/", response_model=list[ShipmentResponse])
def get_shipments(session: Session = Depends(get_session)):

    shipments = session.exec(select(Shipment)).all()

    return shipments


@router.post("/", response_model=ShipmentResponse)
def create_shipment(shipment: ShipmentCreate, session: Session = Depends(get_session)):

    db_shipment = Shipment(**shipment.model_dump())

    session.add(db_shipment)            #Add to database
    session.commit()                    #Save changes
    session.refresh(db_shipment)        #Refresh object from DB

    return db_shipment

@router.get("/{shipment_id}", response_model=ShipmentResponse)
def get_shipment(
    shipment_id: int,
    session: Session = Depends(get_session)
):

    shipment = session.get(Shipment, shipment_id)

    if not shipment:
        return {"error": "Shipment not found"}

    return shipment


@router.delete("/{shipment_id}")
def delete_shipment(
    shipment_id: int,
    session: Session = Depends(get_session)
):

    shipment = session.get(Shipment, shipment_id)

    if not shipment:
        return {"error": "Shipment not found"}

    session.delete(shipment)
    session.commit()

    return {"message": "Shipment deleted"}