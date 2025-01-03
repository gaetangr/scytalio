from database import create_db_and_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import Settings
from routes import encrypt, decrypt
from contextlib import asynccontextmanager
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
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
        allow_origins=Settings.ALLOWED_ORIGINS,
        allow_credentials=Settings.ALLOW_CREDENTIALS,
        allow_methods=Settings.ALLOWED_METHODS,
        allow_headers=Settings.ALLOWED_HEADERS,
    )

    app.include_router(encrypt.router)
    app.include_router(decrypt.router)

    return app


app = create_app()
