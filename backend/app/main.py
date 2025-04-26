from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.questionaire import *

from app.routers import llm

app = FastAPI(
    title="LLM API",
    description="API for LLM-based pet adoption survey",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/redoc")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Default Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home endpoint
@app.get("/", tags=["General"])
def read_root():
    """Returns a welcome message."""
    return {"message": "Welcome to the LLM API!"}

@app.get("/test", tags=["General"], response_model=PetAdoptionSurvey)
def read_test():
    survey = PetAdoptionSurvey(
        grooming_spending=GroomingSpending.MEDIUM,
        running_miles=RunningMiles.RANGE_2_5,
        couch_fur_happiness=4,
        vacuum_times=VacuumTimes.ONE,
        happy_with_large_dogs=True,
        happy_with_small_dogs=False,
        hoa_pet_contract="/path/to/screenshot.png",
        other_pets=[OtherPets.CAT, OtherPets.DOG],
        kids_around_friend=True,
        travel_distance=TravelDistance.FIVE_TO_TEN,
        home_address="123 Main St, Milwaukee, WI",
        paid_transport=True,
        envisioned_age=EnvisionedAge.TWELVE_TO_THIRTY_SIX,
        plan_to_travel=False,
        journey_payment=JourneyPayment.HIGH,
        food_spending=500,
        has_yard=True,
        personality_traits="Energetic, friendly, and playful",
        active_dogs_enjoyment=ActiveDogsEnjoyment.VERY_MUCH,
        value_compatibility=CompatibilityValue.SOMEWHAT,
        cute_dogs=CuteDogsLove.NEUTRAL,
        intact_requirement=None,  # None indicates "doesn't matter"
        only_rescue=True,
        gender_preference=GenderPreference.FEMALE
    )
    return survey

# Include routers
app.include_router(llm.router, prefix="/api") 
