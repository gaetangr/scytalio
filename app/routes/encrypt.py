from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
from app.models import EncryptedContent
from app.services import MessageService
from app.utils import is_base64
from ..database import get_session
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.post(
    "/encrypt",
    response_model=EncryptedContent,
    status_code=status.HTTP_201_CREATED,
)
async def encrypt_message(
    content: EncryptedContent, session: Annotated[Session, Depends(get_session)]
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
