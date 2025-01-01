import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
SQLITE_CONNECT_ARGS = {"check_same_thread": False}


class Settings:
    """Application settings and constants."""

    ALLOWED_ORIGINS: list[str] = ["*"]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    RATE_LIMITING_DEFAULT: int = os.getenv("", 20)
