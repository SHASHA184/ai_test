from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str | None = None
    llm_model_name: str = Field(default="gpt-4")
    llm_temperature: float = Field(default=0.7, ge=0.0, le=1.0)


settings = Settings()
