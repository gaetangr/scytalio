from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from typing import Annotated
from uuid import UUID

from utils import is_base64
from settings import Settings
from constants import APIEndpoints
from models import EncryptedContent
from services import MessageService
from database import get_session
from slowapi.util import get_remote_address
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)


router = APIRouter()


# The request argument must be explicitly passed to
# the endpoint for the rate limiter to work.
@router.get(APIEndpoints.DECRYPT_MESSAGE, response_model=EncryptedContent)
@limiter.limit(f"{Settings().RATE_LIMITING_DEFAULT}/minute")
async def get_message(
    request: Request, message_id: str, session: Annotated[Session, Depends(get_session)]
) -> EncryptedContent:
    """Retrieve an encrypted message by ID."""
    try:
        UUID(message_id)
        return await MessageService.get_message(message_id, session)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid message ID format, UUID expected.",
        )


@router.post(
    APIEndpoints.ENCRYPT_MESSAGE,
    response_model=EncryptedContent,
    status_code=status.HTTP_201_CREATED,
)
@limiter.limit(f"{Settings().RATE_LIMITING_DEFAULT}/minute")
async def create_message(
    request: Request,
    content: EncryptedContent,
    session: Annotated[Session, Depends(get_session)],
) -> EncryptedContent:
    """Create a new encrypted message."""
    try:
        is_base64(content.message)
        return await MessageService.create_message(content, session)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid message format, expected base64 format",
        )


@router.delete(
    APIEndpoints.DELETE_MESSAGE,
    response_model=EncryptedContent,
    status_code=status.HTTP_200_OK,
)
@limiter.limit(f"{Settings().RATE_LIMITING_DEFAULT}/minute")
async def delete_message(
    request: Request,
    message_id: str,
    session: Annotated[Session, Depends(get_session)],
) -> EncryptedContent:
    """Delete an encrypted message."""
    try:
        UUID(message_id)
        return await MessageService.delete_message(message_id, session)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid message ID format, UUID expected.",
        )
