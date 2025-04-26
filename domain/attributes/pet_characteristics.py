from pydantic import BaseModel
from typing import Literal

from constants.attributes import *

class PetCharacteristic(BaseModel):
    activity_level: ActivityLevel
    size: Size
    temperament: Temperament
    fur_type: FurType
    intelligence: IntelligenceLevel
    maintenance: MaintenanceLevel
    breed: str
    species: str
    hypoallergenic: Literal["Y", "N"]