from pydantic import BaseModel
from uuid import UUID
from attributes.contact_info import ContactInfo
from entities.pet import Pet
from typing import List
from relationships.offering import Offering
class Vendor(BaseModel):
    id: UUID 
    name: str
    contactInfo: ContactInfo
    offerings: List[Offering]
