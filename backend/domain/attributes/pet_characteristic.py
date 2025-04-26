from pydantic import BaseModel
from typing import Literal, Optional

from ..constants.attributes import *

class PetCharacteristic(BaseModel):
    activity_level: Optional[ActivityLevel]
    size: Optional[Size]
    temperament: Optional[Temperament]
    fur_type: Optional[FurType]
    intelligence: Optional[IntelligenceLevel]
    maintenance: Optional[MaintenanceLevel]
    breed: Optional[str]
    species: str
