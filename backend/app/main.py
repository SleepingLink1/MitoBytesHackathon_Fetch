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

@app.get("/survey", tags=["Pet Adoption Survey"])
def read_survey(): 
    fields = PetAdoptionSurvey.__annotations__
    response = []

    for field_name, field_type in fields.items():
        field_info = PetAdoptionSurvey.__fields__.get(field_name)
        if isinstance(field_type, type) and issubclass(field_type, Enum):
            enum_values = [{"key": e.name, "value": e.value} for e in field_type]  # Extract enum values
        else:
            enum_values = None

        response_item = {
            "name": field_name,
            "description": field_info.description if field_info else "",
            "responseType": "options" if enum_values else "boolean" if field_type == bool else "string",
            "options": enum_values,
        }
        response.append(response_item)

    return response

@app.post("/test", tags=["General"], response_model=PetAdoptionSurvey)
def read_test(survey: PetAdoptionSurvey):
 
    return survey

# Include routers
app.include_router(llm.router, prefix="/api") 
