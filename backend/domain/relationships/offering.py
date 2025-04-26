from pydantic import BaseModel, Field
from uuid import uuid4, UUID
from entities.pet import Pet

from ..constants.attributes import Availability
class Offering (BaseModel):
    id: UUID =  Field(default_factory=lambda: str(uuid4()))
    price: float
    pet: Pet
    availability: Availability
    