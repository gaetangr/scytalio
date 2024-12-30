from app.database import create_db_and_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import Settings
from app.routes import encrypt, decrypt


def create_app() -> FastAPI:
    app = FastAPI(
        title="Encrypted Messages API",
        description="API for storing and retrieving encrypted messages",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=Settings.ALLOWED_ORIGINS,
        allow_credentials=Settings.ALLOW_CREDENTIALS,
        allow_methods=Settings.ALLOWED_METHODS,
        allow_headers=Settings.ALLOWED_HEADERS,
    )

    # Routes
    app.include_router(encrypt.router)
    app.include_router(decrypt.router)

    @app.on_event("startup")
    def on_startup() -> None:
        """Initialize database on startup."""
        create_db_and_tables()

    return app


app = create_app()
