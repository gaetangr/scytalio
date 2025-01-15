from sqlmodel import SQLModel, create_engine, Session
from settings import Settings
from typing import Generator

settings = Settings()

engine = create_engine(settings.DATABASE_URL, echo=False)


def create_db_and_tables() -> None:
    """
    Create the database and tables.

    This function initializes the database and creates all the tables
    defined in the SQLModel metadata.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Get a database session.

    This function provides a generator that yields a database session.
    It ensures that the session is properly closed after use.

    Yields:
        Generator[Session, None, None]: A generator yielding a database session.
    """
    with Session(engine) as session:
        yield session
