from enum import Enum


class ShipmentStatus(str, Enum):
    CREATED = "Created"
    DEPARTED = "Departed"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"