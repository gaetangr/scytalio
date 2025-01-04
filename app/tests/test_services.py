from unittest.mock import MagicMock
import pytest
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from models import EncryptedContent
from services import MessageService


@pytest.mark.asyncio
async def test_create_message_success(session, encrypted_content):
    session.add = MagicMock()
    session.commit = MagicMock()
    session.refresh = MagicMock()

    result = await MessageService.create_message(encrypted_content, session)

    session.add.assert_called_once()
    session.commit.assert_called_once()
    session.refresh.assert_called_once()
    assert result.message == encrypted_content.message
    assert result.iv == encrypted_content.iv


@pytest.mark.asyncio
async def test_create_message_empty_content(session):
    empty_content = EncryptedContent(message="", iv="test_iv")

    with pytest.raises(HTTPException) as exc_info:
        await MessageService.create_message(empty_content, session)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc_info.value.detail == "Message cannot be empty"


@pytest.mark.asyncio
async def test_create_message_integrity_error(session, encrypted_content):
    session.add = MagicMock()
    session.commit = MagicMock(side_effect=IntegrityError(None, None, None))
    session.rollback = MagicMock()

    with pytest.raises(HTTPException) as exc_info:
        await MessageService.create_message(encrypted_content, session)

    session.rollback.assert_called_once()
    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc_info.value.detail == "Message creation failed due to integrity error"


@pytest.mark.asyncio
async def test_get_message_success(session, encrypted_content):
    session.get = MagicMock(return_value=encrypted_content)
    session.delete = MagicMock()
    session.commit = MagicMock()

    result = await MessageService.get_message("test_id", session)

    session.get.assert_called_once_with(EncryptedContent, "test_id")
    session.delete.assert_called_once_with(encrypted_content)
    session.commit.assert_called_once()
    assert result.message == encrypted_content.message
    assert result.iv == encrypted_content.iv


@pytest.mark.asyncio
async def test_get_message_not_found(session):
    session.get = MagicMock(return_value=None)

    with pytest.raises(HTTPException) as exc_info:
        await MessageService.get_message("test_id", session)

    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
    assert exc_info.value.detail == "Message not found"


@pytest.mark.asyncio
async def test_get_message_delete_error(session, encrypted_content):
    session.get = MagicMock(return_value=encrypted_content)
    session.delete = MagicMock()
    session.commit = MagicMock(side_effect=Exception)
    session.rollback = MagicMock()

    with pytest.raises(HTTPException) as exc_info:
        await MessageService.get_message("test_id", session)

    session.rollback.assert_called_once()
    assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert (
        exc_info.value.detail
        == "An error occurred while deleting the message after reading."
    )


@pytest.mark.asyncio
async def test_create_message_invalid_format(session):
    invalid_content = EncryptedContent(message="invalid_base64_message", iv="test_iv")

    with pytest.raises(HTTPException) as exc_info:
        await MessageService.create_message(invalid_content, session)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc_info.value.detail == "Invalid message format, expected base64 format"


@pytest.mark.asyncio
async def test_get_message_invalid_format(session):
    invalid_message_id = "invalid_uuid"

    with pytest.raises(HTTPException) as exc_info:
        await MessageService.get_message(invalid_message_id, session)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc_info.value.detail == "Invalid message ID format, UUID expected."
