from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    GEMINI_SECRET_KEY: str


settings = Setting()
