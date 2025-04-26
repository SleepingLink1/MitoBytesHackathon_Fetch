from pydantic import BaseModel
from uuid import UUID
from typing import List 

from ..entities.pet import Pet
from ..attributes.pet_characteristics import PetCharacteristic
from ..attributes.contact_info import ContactInfo

class Customer(BaseModel):
    id: UUID
    name:str
    contactInfo:ContactInfo
    petRestrictions: PetCharacteristic
    currentPets: List[Pet]
    