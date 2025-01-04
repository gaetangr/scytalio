from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session
from typing import Annotated
from models import EncryptedContent
from services import MessageService
from utils import is_base64
from database import get_session
from fastapi import HTTPException
from slowapi.util import get_remote_address
from slowapi import Limiter
from settings import Settings

router = APIRouter()

limiter = Limiter(key_func=get_remote_address)


# The request argument must be explicitly passed to
# the endpoint for the rate limiter to work.
@router.post(
    "/encrypt",
    response_model=EncryptedContent,
    status_code=status.HTTP_201_CREATED,
)
@limiter.limit(f"{Settings.RATE_LIMITING_DEFAULT}/minute")
async def encrypt_message(
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
