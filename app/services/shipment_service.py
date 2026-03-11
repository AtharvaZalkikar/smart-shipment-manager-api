from sqlmodel import Session, select
from app.models.shipment import Shipment

from sqlmodel import select, desc



def create_shipment(session: Session, shipment_data: dict):

    db_shipment = Shipment(**shipment_data)

    session.add(db_shipment)
    session.commit()
    session.refresh(db_shipment)

    return db_shipment

def get_shipments(
    session,
    limit=10,
    offset=0,
    sort_by="id",
    order="asc",
    status=None,
    destination=None
):

    allowed_fields = {"id", "destination", "status"}

    if sort_by not in allowed_fields:
        raise ValueError("Invalid sort field")

    column = getattr(Shipment, sort_by)

    if order == "desc":
        column = desc(column)

    query = select(Shipment)

    # filtering
    if status:
        query = query.where(Shipment.status == status)

    if destination:
        query = query.where(Shipment.destination == destination)

    shipments = session.exec(
        query
        .order_by(column)
        .offset(offset)
        .limit(limit)
    ).all()

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

def update_shipment(session, shipment_id: int, update_data: dict):

    shipment = session.get(Shipment, shipment_id)

    if not shipment:
        return None

    for key, value in update_data.items():
        setattr(shipment, key, value)

    session.add(shipment)
    session.commit()
    session.refresh(shipment)

    return shipment