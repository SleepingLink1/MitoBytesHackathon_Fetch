from pydantic import BaseModel, Field
from uuid import uuid4, UUID
from typing import List 

from ..entities.pet import Pet
from ..attributes.pet_characteristic import PetCharacteristic
from ..attributes.contact_info import ContactInfo

class Customer(BaseModel):
    id: UUID =  Field(default_factory=lambda: str(uuid4()))
    name:str
    contactInfo:ContactInfo
    petRestrictions: PetCharacteristic
    currentPets: List[Pet]
    