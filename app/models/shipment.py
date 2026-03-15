from sqlmodel import SQLModel, Field
from app.models.shipment_status import ShipmentStatus
from datetime import datetime, timezone
from sqlalchemy import Index

from sqlmodel import SQLModel, Field
from sqlalchemy import Index
from app.models.shipment_status import ShipmentStatus
from datetime import datetime, timezone


class Shipment(SQLModel, table=True):

    __table_args__ = (
        Index("idx_shipment_destination", "destination"),
        Index("idx_shipment_status", "status"),
        Index("idx_shipment_created_at", "created_at"),
    )

    id: int | None = Field(default=None, primary_key=True)

    destination: str

    status: ShipmentStatus = Field(default=ShipmentStatus.CREATED)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    updated_at: datetime | None = Field(default=None)