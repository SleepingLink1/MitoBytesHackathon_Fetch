from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

from app.services.questionaire import *

from app.routers import llm
import PetFinderAPI

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


@app.get("/getPets/", tags=["General"])
def get_pets():
    search_params = {
        'type': 'dog',
        'location': 'Milwaukee, WI',
        'limit': 5,
        'distance': 10,
        'status': 'adoptable' # Only show adoptable pets
    }
    message = PetFinderAPI.make_api_call("/animals", params=search_params)
    animals = message.get("animals", [])

    # Now filter the fields you care about
    filtered_animals = []
    for animal in animals:
        filtered_animals.append({
            "id": animal.get("id"),
            "name": animal.get("name"),
          "species": animal.get("species"),
            "breeds": animal.get("breeds"),
            "sex": animal.get("sex"),
            "age": animal.get("age"),
            "petChar":{
                "activity_level": animal.get("activity_level"),
                "size": animal.get("size"),
                "temperament": animal.get("temperament"),
                "fur_type": animal.get("coat"),
                "intelligence": animal.get("intelligence"),
                "maintenance": animal.get("maintenance"),
                "breed": animal.get("breeds"),
                "species": animal.get("species"),
                "hypoallergenic": animal.get("hypoallergenic"),
            }

            # "coat": animal.get("coat"),
            # "size": animal.get("size"),
            # "environment": animal.get("environment"),
            # "distance": animal.get("distance"),
            # "age": animal.get("age"),
            # "tags": animal.get("tags"),
            # "gender": animal.get("gender")
         
        })

    return {"pets": filtered_animals}

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
