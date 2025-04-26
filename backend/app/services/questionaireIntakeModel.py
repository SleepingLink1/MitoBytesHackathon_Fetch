from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

# --- Enum Definitions for Discrete Choices ---

class GroomingSpending(Enum):
    LOW = "$0-50"
    MEDIUM = "$50-100"
    HIGH = "$100+"

class RunningMiles(Enum):
    RANGE_0_1 = "0-1"
    RANGE_2_5 = "2-5"
    RANGE_5_PLUS = "5+"

class VacuumTimes(Enum):
    ZERO = "0"
    ONE = "1"
    THREE_PLUS = "3+"

class TravelDistance(Enum):
    ZERO_MILES = "0 miles"
    UP_TO_FIVE = "up to 5"
    FIVE_TO_TEN = "5-10"
    TEN_PLUS = "10+"

class EnvisionedAge(Enum):
    ZERO_TO_FIVE = "0-5months"
    FIVE_TO_TWELVE = "5-12months"
    TWELVE_TO_THIRTY_SIX = "12-36months"
    THIRTY_SIX_PLUS = "36months+"

class JourneyPayment(Enum):
    LOW = "$0-$50"
    MEDIUM = "$50-500"
    HIGH = "$500-1000"
    VERY_HIGH = "$1000+"

class ActiveDogsEnjoyment(Enum):
    VERY_MUCH = "very much"
    SOMEWHAT = "somewhat"
    NEUTRAL = "neutral"
    A_LITTLE = "a little"
    NOT_AT_ALL = "not at all"

class CompatibilityValue(Enum):
    VERY_MUCH = "very much"
    SOMEWHAT = "somewhat"
    NEUTRAL = "neutral"
    A_LITTLE = "a little"
    NOT_AT_ALL = "not at all"

class CuteDogsLove(Enum):
    VERY_MUCH = "very much"
    SOMEWHAT = "somewhat"
    NEUTRAL = "neutral"
    A_LITTLE = "a little"
    NOT_AT_ALL = "not at all"

class OtherPets(Enum):
    CAT = "cat"
    DOG = "dog"
    EXOTIC = "Exotic"
    OTHER_DOMESTIC = "other domestic pet"

class GenderPreference(Enum):
    FEMALE = "a female"
    MALE = "a male"

# --- Pydantic Model for Returning Responses ---

class QuestionaireModel(BaseModel):
    grooming_spending: GroomingSpending
    running_miles: RunningMiles
    couch_fur_happiness: int
    vacuum_times: VacuumTimes
    happy_with_large_dogs: bool
    happy_with_small_dogs: bool
    hoa_pet_contract: str
    other_pets: List[OtherPets]
    kids_around_friend: bool
    travel_distance: TravelDistance
    home_address: str
    paid_transport: bool
    envisioned_age: EnvisionedAge
    plan_to_travel: bool
    journey_payment: JourneyPayment
    food_spending: int
    has_yard: bool
    personality_traits: str
    active_dogs_enjoyment: ActiveDogsEnjoyment
    value_compatibility: CompatibilityValue
    cute_dogs: CuteDogsLove
    intact_requirement: Optional[bool]
    only_rescue: bool
    gender_preference: GenderPreference

    class Config:
        use_enum_values = False

    def dict(self, **kwargs):
        """
        Override the default dict() method to return enum names instead of values.
        """
        original_dict = super().dict(**kwargs)
        for key, value in original_dict.items():
            if isinstance(value, Enum): 
                original_dict[key] = value.name 
            elif isinstance(value, list): 
                original_dict[key] = [
                    item.name if isinstance(item, Enum) else item for item in value
                ]
        return original_dict