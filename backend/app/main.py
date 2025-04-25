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

# Include routers
app.include_router(llm.router, prefix="/api") 