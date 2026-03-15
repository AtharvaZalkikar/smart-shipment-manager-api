from sqlmodel import SQLModel, Field
from app.models.shipment_status import ShipmentStatus
from datetime import datetime, timezone

class Shipment(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    destination: str
    status: ShipmentStatus = Field(default=ShipmentStatus.CREATED) #updated from str to use ENUMS in shipment_status.py

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  #default_factory generates a new timestamp for every row.

    updated_at: datetime | None = Field(default=None)