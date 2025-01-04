from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv
from typing import Generator
from models import EncryptedContent

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./scytalio.db")
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
    EncryptedContent.create_index(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
