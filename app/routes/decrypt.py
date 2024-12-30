from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated
from uuid import UUID

from ..models import EncryptedContent
from ..services import MessageService
from ..database import get_session

router = APIRouter()


@router.get("/decrypt/{message_id}", response_model=EncryptedContent)
async def get_encrypted_message(
    message_id: str, session: Annotated[Session, Depends(get_session)]
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
