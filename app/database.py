from sqlmodel import SQLModel, create_engine, Session
from settings import Settings
from typing import Generator
from models import EncryptedContent

settings = Settings()

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
    EncryptedContent.create_index(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
