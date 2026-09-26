from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI-SOC"
    api_v1_prefix: str = "/api"
    debug: bool = True
    database_url: str = "sqlite:///./ai_soc.db"
    jwt_secret: str = "dev-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    demo_mode: bool = True
    use_mock_threat_intel: bool = True

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
