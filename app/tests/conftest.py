from fastapi.testclient import TestClient
import pytest
from sqlmodel import Session
from sqlalchemy.orm import sessionmaker


from app.database import create_db_and_tables, engine
import pytest
from app.main import app

# This conftest.py file is used by pytest to define shared fixtures
# across multiple test files. Fixtures allow you to set up states
# or resources needed for tests and reuse them in different tests.
# https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def session():
    create_db_and_tables()
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
