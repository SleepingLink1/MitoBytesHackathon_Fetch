from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import llm

app = FastAPI(title="LLM API")

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

@app.get("/getPets", tags=["General"])
def read_root():
    search_params = {
        'type': 'dog',
        'location': 'Milwaukee, WI',
        'limit': 5,
        'distance': 20,
        'status': 'adoptable' # Only show adoptable pets
    }
    message = PetFinderAPI.make_api_call("/animals", params=search_params)
    return {"message": message}

 


# Include routers
app.include_router(llm.router, prefix="/api") 