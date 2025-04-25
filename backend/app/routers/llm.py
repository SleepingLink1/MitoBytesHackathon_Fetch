from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_client import get_llm_client

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=AnswerResponse)
async def ask_llm(request: QuestionRequest):
    try:
        llm_client = get_llm_client()
        answer = llm_client.get_response(request.question)
        return AnswerResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {str(e)}") 