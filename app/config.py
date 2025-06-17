from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.app_name = "Clothing Analysis API"
        self.version = "1.0.0"
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4-vision-preview")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "1000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.cors_origins = ["*"]


@lru_cache()
def get_settings():
    return Settings()