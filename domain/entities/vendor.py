from pydantic import BaseModel
from uuid import UUID
from attributes.contact_info import ContactInfo
from entities.pet import Pet
from typing import List
class Vendor(BaseModel):
    id: UUID 
    name: str
    location: str
    contact_info: ContactInfo
    pets: List[Pet] 
