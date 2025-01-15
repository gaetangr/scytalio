from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from typing import Annotated
from uuid import UUID

from sqlmodel import select

from utils import is_base64
from settings import Settings
from constants import APIEndpoints
from models import EncryptedContent, WebsiteStats
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
    """
    Retrieve an encrypted message by ID.

    Args:
        request (Request): The request object.
        message_id (str): The ID of the encrypted message.
        session (Annotated[Session, Depends(get_session)]): The database session.

    Returns:
        EncryptedContent: The encrypted message.

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
    """
    Create a new encrypted message.

    Args:
        request (Request): The request object.
        content (EncryptedContent): The encrypted message content.
        session (Annotated[Session, Depends(get_session)]): The database session.

    Returns:
        EncryptedContent: The created encrypted message.

    Raises:
        HTTPException: If the message format is invalid.
    """
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
    """
    Delete an encrypted message.

    Args:
        request (Request): The request object.
        message_id (str): The ID of the encrypted message.
        session (Annotated[Session, Depends(get_session)]): The database session.

    Returns:
        EncryptedContent: The deleted encrypted message.

    Raises:
        HTTPException: If the authorization header is missing or invalid, or if the message ID format is invalid.
    """
    authorization_header_hmac = request.headers.get("Authorization")
    expected_hmac = session.get(EncryptedContent, message_id).hmac
    if not authorization_header_hmac or authorization_header_hmac != expected_hmac:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    try:
        UUID(message_id)
        return await MessageService.delete_message(message_id, session)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid message ID format, UUID expected.",
        )


@router.get(
    "/stats",
    response_model=WebsiteStats,
    summary="Get website statistics",
    description="Retrieve global statistics about website usage",
)
async def get_website_stats(session: Session = Depends(get_session)):
    """
    Get global website statistics.

    Args:
        session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        WebsiteStats: The global website statistics.
    """
    stats = session.exec(
        select(WebsiteStats).where(WebsiteStats.id == "global_stats")
    ).first()
    if not stats:
        stats = WebsiteStats()
        session.add(stats)
        await session.commit()
        await session.refresh(stats)
    return stats
