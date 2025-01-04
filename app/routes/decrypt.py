from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from typing import Annotated
from uuid import UUID

from settings import Settings

from models import EncryptedContent
from services import MessageService
from database import get_session
from slowapi.util import get_remote_address
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)


router = APIRouter()


# The request argument must be explicitly passed to
# the endpoint for the rate limiter to work.
@router.get("/decrypt/{message_id}", response_model=EncryptedContent)
@limiter.limit(f"{Settings().RATE_LIMITING_DEFAULT}/minute")
async def get_encrypted_message(
    request: Request, message_id: str, session: Annotated[Session, Depends(get_session)]
) -> EncryptedContent:
    """
    Retrieve an encrypted message by ID.

    This endpoint accepts a message ID in UUID format and retrieves the corresponding encrypted message from the database.
    It validates the message ID format and returns the encrypted message content.

    Args:
        request (Request): The request object.
        message_id (str): The ID of the encrypted message.
        session (Session): The database session.

    Returns:
        EncryptedContent: The retrieved encrypted message content.

    Raises:
        HTTPException: If the message ID format is invalid or the message is not found.
    """
    try:
        UUID(message_id)
        return await MessageService.get_message(message_id, session)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid message ID format, UUID expected.",
        )
