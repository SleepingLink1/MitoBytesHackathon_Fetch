from pydantic import BaseModel, Field
from uuid import uuid4, UUID

from ..attributes.pet_characteristic import PetCharacteristic
from ..constants.attributes import Sex
class Pet(BaseModel):
     id: UUID =  Field(default_factory=lambda: str(uuid4()))
     name: str
     species: str  # e.g., Dog, Cat
     breed: str
     sex: Sex
     age: int
     petChar:PetCharacteristic

