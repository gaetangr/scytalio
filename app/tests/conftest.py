from fastapi.testclient import TestClient
import pytest
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.pool import StaticPool

from app.main import app

# This conftest.py file is used by pytest to define shared fixtures
# across multiple test files. Fixtures allow you to set up states
# or resources needed for tests and reuse them in different tests.
# https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files


@pytest.fixture(scope="session")
def engine():
    engine = create_engine(
        "sqlite:///./test.db",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session
        session.rollback()


@pytest.fixture
def client():
    return TestClient(app)
