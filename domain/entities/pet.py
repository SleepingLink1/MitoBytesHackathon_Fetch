from pydantic import BaseModel
from uuid import UUID
class Pet(BaseModel):
     id: UUID
     name: str
     species: str  # e.g., Dog, Cat
     breed: str
     age: int
     vendor_id: str  # Owner vendor id

