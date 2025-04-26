from pydantic import BaseModel
from uuid import UUID
from entities.pet import Pet

from ..constants.attributes import Availability
class Offering (BaseModel):
    id: UUID
    price: float
    pet: Pet
    availability: Availability
    