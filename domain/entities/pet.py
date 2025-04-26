from pydantic import BaseModel
from uuid import UUID

from ..attributes.pet_characteristics import PetCharacteristic
from ..constants.attributes import Sex
class Pet(BaseModel):
     id: UUID
     name: str
     species: str  # e.g., Dog, Cat
     breed: str
     sex: Sex
     age: int
     petChar:PetCharacteristic

