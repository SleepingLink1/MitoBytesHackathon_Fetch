from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, conint, Field

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

# --- Pydantic Survey Model ---

class PetAdoptionSurvey(BaseModel):
    grooming_spending: GroomingSpending = Field(
        ..., description="How much am I willing to spend bimonthly on professional grooming?"
    )
    running_miles: RunningMiles = Field(
        ..., description="How many miles am I willing to run everyday?"
    )
    # Using a constrained int to ensure the happiness rating is between 1 and 5.
    couch_fur_happiness: conint(ge=1, le=5) = Field(
        ..., description="On a scale of 1-5, how happy do I feel removing fur from my couch?"
    )
    vacuum_times: VacuumTimes = Field(
        ..., description="How many times a day am I willing to vacuum?"
    )
    happy_with_large_dogs: bool = Field(
        ..., description="When I hang out with or see large dogs I feel happy."
    )
    happy_with_small_dogs: bool = Field(
        ..., description="When I hang out with or see small dogs I feel happy."
    )
    other_pets: List[OtherPets] = Field(
        ..., description="I have other pets or plan to have other pets."
    )
    kids_around_friend: bool = Field(
        ..., description="I have kids or plan to have kids around my future best friend."
    )
    travel_distance: TravelDistance = Field(
        ..., description="I am willing to travel in order to pick up my future best friend."
    )
    home_address: str = Field(
        ..., description="Enter my home address here."
    )
    paid_transport: bool = Field(
        ..., description="I am willing to pay someone to transport my future best friend."
    )
    envisioned_age: EnvisionedAge = Field(
        ..., description="The age I envision my future best friend to be."
    )
    plan_to_travel: bool = Field(
        ..., description="I plan to travel with my future best friend."
    )
    journey_payment: JourneyPayment = Field(
        ..., description="I am willing to pay this amount to begin my happiness journey."
    )
    # Food spending is an integer between 0 and 1000.
    food_spending: conint(ge=0, le=1000) = Field(
        ..., description="How much am I willing to spend on food every month?"
    )
    has_yard: bool = Field(
        ..., description="I have a yard to play with my future best friend in."
    )
    personality_traits: str = Field(
        ..., description="Sociability, temperament, personality."
    )
    active_dogs_enjoyment: ActiveDogsEnjoyment = Field(
        ..., description="I enjoy active dogs."
    )
    value_compatibility: CompatibilityValue = Field(
        ..., description="I value a dog who gets along well with others."
    )
    cute_dogs: CuteDogsLove = Field(
        ..., description="I love cute dogs."
    )
    # For intact_requirement, True means "yes," False means "no," and None means "doesn't matter."
    intact_requirement: Optional[bool] = Field(
        None, description="I want a dog that is intact (not spade or neutered)."
    )
    only_rescue: bool = Field(
        ..., description="I only want a dog that is a rescue."
    )
    gender_preference: GenderPreference = Field(
        ..., description="I want my future best friend to be of the preferred gender."
    )