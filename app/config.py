from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Clothing Analysis API"
    version: str = "1.0.0"
    openai_api_key: str
    openai_model: str = "gpt-4-vision-preview"
    max_tokens: int = 1000
    temperature: float = 0.7
    
    cors_origins: list[str] = ["*"]
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()