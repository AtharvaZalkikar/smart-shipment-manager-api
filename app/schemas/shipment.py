from pydantic import BaseModel #pydantic models
from typing import Optional

'''
What request_model Does:

validates the input from the user
'''
# ShipmentCreate → request schema
class ShipmentCreate(BaseModel):
    destination: str
    status: str

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

# ShipmentResponse → response schema
class ShipmentUpdate(BaseModel):
    status: Optional[str] = None
    destination: Optional[str] = None