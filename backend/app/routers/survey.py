from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_client import get_llm_client

from app.services.questionaire import *
from app.services.questionaireIntakeModel import *

router = APIRouter()

@router.get("/survey", tags=["Pet Adoption Survey"])
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

@router.post("/submit-survey")
async def post_survey(survey: QuestionaireModel):
    try:
        print(survey)
        
        # llm_client = get_llm_client()
        # llm_client.get_response("Let's get the jupiter book going here")
        
        return {"message": "Survey posted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}")

