"""Define environment-based application settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Load application settings, including the Gemini API key, from the environment."""

    app_name: str = 'AI Systems Lab'
    environment: str = Field(default='local', description='local development')
    debug: bool = False
    gemini_api_key: str = Field(min_length=1, validation_alias='GEMINI_API_KEY')

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
    )
