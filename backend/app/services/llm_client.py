from langchain_openai import OpenAI
from app.config import settings

class LLMClient:
    def __init__(self):
        self.llm = OpenAI(
            api_key=settings.llm_api_key,
            temperature=settings.temperature,
            model_name=settings.model_name,
            max_tokens=settings.max_tokens
        )
    
    def get_response(self, question: str) -> str:
        """Get a response from the LLM."""
        try:
            return self.llm.invoke(question)
        except Exception as e:
            # Log the error here if needed
            raise Exception(f"Failed to get response from LLM: {str(e)}")

def get_llm_client() -> LLMClient:
    """Factory function to get an LLM client instance."""
    return LLMClient() 