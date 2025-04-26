from pydantic import BaseModel, Field
from uuid import uuid4, UUID
from typing import List

from ..relationships.offering import Offering
from ..attributes.contact_info import ContactInfo
class Vendor(BaseModel):
    id: UUID =  Field(default_factory=lambda: str(uuid4()))
    name: str
    contactInfo: ContactInfo
    offerings: List[Offering]
