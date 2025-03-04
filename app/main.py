from utils import generate_static_docs
from database import create_db_and_tables
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from settings import Settings
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from routes import router


settings = Settings()


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    This function sets up the FastAPI application, including database
    initialization, rate limiting, CORS middleware, and route inclusion.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """
    def lifespan(app: FastAPI):
        """
        Lifespan context for the FastAPI application.

        This context is used to perform setup and teardown tasks for the
        application, such as creating database tables.

        Args:
            app (FastAPI): The FastAPI application instance.
        """
        create_db_and_tables()
        try:
            yield
        finally:
            pass

    limiter = Limiter(key_func=get_remote_address)

    app = FastAPI(
        title="Encrypted Messages API",
        description="API for storing and retrieving encrypted messages",
        version="1.0.0",
        lifespan=lifespan,
    )

    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.ALLOW_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    generate_static_docs(app, "app/static")
