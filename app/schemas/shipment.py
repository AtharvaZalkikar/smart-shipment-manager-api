from pydantic import BaseModel #pydantic models
from typing import Optional
from app.models.shipment_status import ShipmentStatus
from datetime import datetime

'''
What request_model Does:

validates the input from the user
'''
# ShipmentCreate → request schema
class ShipmentCreate(BaseModel):
    destination: str
    #status: ShipmentStatus     #using ENUMS (preset values now)

'''
What response_model Does:

1 Validate response data
2 Filter unwanted fields
3 Improve Swagger docs
4 Generate OpenAPI schema
'''
# ShipmentResponse → response schema
class ShipmentResponse(BaseModel):   #in production we want to control the response structure
    id: int
    destination: str
    status: str
    created_at: datetime   #timestamp added

# ShipmentResponse → response schema
class ShipmentUpdate(BaseModel):
    status: Optional[ShipmentStatus] = None #using ENUMS (preset values now)
    destination: Optional[str] = None

# ShipmentResponse (pagination) → Pagination response schema
class ShipmentListResponse(BaseModel):
    items: list[ShipmentResponse]
    total: int
    limit: int
    offset: int