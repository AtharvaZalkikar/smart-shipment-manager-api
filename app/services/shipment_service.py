from sqlmodel import Session, select
from app.models.shipment import Shipment


def create_shipment(session: Session, shipment_data: dict):

    db_shipment = Shipment(**shipment_data)

    session.add(db_shipment)
    session.commit()
    session.refresh(db_shipment)

    return db_shipment


def get_shipments(session: Session):

    shipments = session.exec(select(Shipment)).all()

    return shipments


def get_shipment(session: Session, shipment_id: int):

    shipment = session.get(Shipment, shipment_id)

    return shipment


def delete_shipment(session: Session, shipment_id: int):

    shipment = session.get(Shipment, shipment_id)

    if not shipment:
        return None

    session.delete(shipment)
    session.commit()

    return shipment