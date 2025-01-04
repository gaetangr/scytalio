from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings and constants."""

    DEBUG: bool = False
    ALLOWED_ORIGINS: list[str] = ["*"]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    RATE_LIMITING_DEFAULT: int = 20
    DATABASE_URL: str = "sqlite:///database.db"
    SQLITE_CONNECT_ARGS: dict = {"check_same_thread": False}

    class Config:
        env_file = ".env"
