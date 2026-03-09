from sqlmodel import SQLModel, Field


class Shipment(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    destination: str
    status: str