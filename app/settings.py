from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings and constants.

    This class defines the configuration settings for the application,
    including database URL, allowed origins, methods, headers, and rate limiting.

    Attributes:
        DEBUG (bool): Flag to enable or disable debug mode.
        ALLOWED_ORIGINS (list[str]): List of allowed origins for CORS.
        ALLOWED_METHODS (list[str]): List of allowed HTTP methods for CORS.
        ALLOWED_HEADERS (list[str]): List of allowed HTTP headers for CORS.
        ALLOW_CREDENTIALS (bool): Flag to allow or disallow credentials in CORS.
        RATE_LIMITING_DEFAULT (int): Default rate limit for requests per minute.
        DATABASE_URL (str): URL for the database connection.
    """

    DEBUG: bool = False
    ALLOWED_ORIGINS: list[str] = ["*"]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    RATE_LIMITING_DEFAULT: int = 20
    DATABASE_URL: str = None

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
