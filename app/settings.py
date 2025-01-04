from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings and constants."""

    DEBUG: bool = Field(default=False, env="DEBUG")
    ALLOWED_ORIGINS: list[str] = Field(default=["*"], env="ALLOWED_ORIGINS")
    ALLOWED_METHODS: list[str] = Field(default=["*"], env="ALLOWED_METHODS")
    ALLOWED_HEADERS: list[str] = Field(default=["*"], env="ALLOWED_HEADERS")
    ALLOW_CREDENTIALS: bool = Field(default=True, env="ALLOW_CREDENTIALS")
    RATE_LIMITING_DEFAULT: int = Field(default=20, env="RATE_LIMITING_DEFAULT")
    DATABASE_URL: str = Field(default="sqlite:///database.db", env="DATABASE_URL")
    SQLITE_CONNECT_ARGS: dict = Field(default={"check_same_thread": False}, env="SQLITE_CONNECT_ARGS")

    class Config:
        env_file = ".env"
