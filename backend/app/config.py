from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    llm_api_key: str = ""
    model_name: str = "gpt-3.5-turbo-instruct"
    temperature: float = 0.7
    max_tokens: int = 1024
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
        
        # Map environment variables to settings
        env_mapping = {
            "OPENAI_API_KEY": "llm_api_key",
            "LLM_API_KEY": "llm_api_key",
            "MODEL_NAME": "model_name",
            "TEMPERATURE": "temperature",
            "MAX_TOKENS": "max_tokens",
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Try both possible environment variable names
        if not self.llm_api_key:
            import os
            self.llm_api_key = os.getenv("OPENAI_API_KEY", "") or os.getenv("LLM_API_KEY", "")

# Create settings instance
settings = Settings() 