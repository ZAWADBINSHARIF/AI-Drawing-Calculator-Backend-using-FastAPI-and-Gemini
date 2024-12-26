from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_SECRET_KEY: str
    GenKey: str = Field(alias="GEMINI_SECRET_KEY")

    class Config:
        env_file = ".env"


settings = Settings()
