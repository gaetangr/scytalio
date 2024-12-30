# Constants
DATABASE_URL = "sqlite:///database.db"
SQLITE_CONNECT_ARGS = {"check_same_thread": False}


class Settings:
    """Application settings and constants."""

    ALLOWED_ORIGINS = ["*"]
    ALLOWED_METHODS = ["*"]
    ALLOWED_HEADERS = ["*"]
    ALLOW_CREDENTIALS = True
