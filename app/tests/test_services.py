from fastapi import HTTPException, status
import pytest
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from app.models import EncryptedContent
from app.services import MessageService


@pytest.mark.asyncio
async def test_create_message(session: Session):
    content = EncryptedContent(message="test message", iv="test_iv")
    created_message = await MessageService.create_message(content, session)

    assert created_message.message == content.message
    assert created_message.iv == content.iv
    assert created_message.id is not None

    # Verify the message is actually in the database
    db_message = session.get(EncryptedContent, created_message.id)
    assert db_message is not None
    assert db_message.message == content.message
    assert db_message.iv == content.iv


@pytest.mark.asyncio
async def test_get_message(session: Session):
    # Create a message to retrieve
    content = EncryptedContent(message="test message", iv="test_iv")
    created_message = await MessageService.create_message(content, session)

    # Retrieve the message by ID
    retrieved_message = await MessageService.get_message(created_message.id, session)

    assert retrieved_message.message == content.message
    assert retrieved_message.iv == content.iv
    assert retrieved_message.id == created_message.id


@pytest.mark.asyncio
async def test_get_message_not_found(session: Session):
    # Try to retrieve a message with a non-existent ID
    non_existent_id = "non-existent-id"
    with pytest.raises(HTTPException) as exc_info:
        await MessageService.get_message(non_existent_id, session)

    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
    assert exc_info.value.detail == "Message not found"
