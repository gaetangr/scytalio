from fastapi.testclient import TestClient
import pytest
from sqlmodel import SQLModel, Session

from models import EncryptedContent

from app.database import engine, get_session
from app.main import app
from app.settings import Settings

# This conftest.py file is used by pytest to define shared fixtures
# across multiple test files. Fixtures allow you to set up states
# or resources needed for tests and reuse them in different tests.
# https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files


@pytest.fixture
def encrypted_content():
    """Fixture pour créer un message encodé en base64 valide"""
    return EncryptedContent(
        message="SGVsbG8gd29ybGQ=",
        iv="test_iv",
    )


@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        yield session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
