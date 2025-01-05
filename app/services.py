from fastapi import HTTPException, status
from sqlmodel import Session
from constants import ErrorMessages
from models import EncryptedContent
from sqlalchemy.exc import IntegrityError


# NOTE: Is @staticmethod make sense here ?
class MessageService:
    """Business logic for message handling"""

    @staticmethod
    async def create_message(
        content: EncryptedContent, session: Session
    ) -> EncryptedContent:
        """Create a new encrypted message."""
        encrypted_message = EncryptedContent(message=content.message, iv=content.iv)
        if not encrypted_message.message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Message cannot be empty",
            )
        try:
            session.add(encrypted_message)
            session.commit()
            session.refresh(encrypted_message)
            return EncryptedContent.model_validate(encrypted_message)
        except IntegrityError:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMessages.INTEGRITY_ERROR,
            )

    @staticmethod
    async def get_message(message_id: str, session: Session) -> EncryptedContent:
        """Retrieve an encrypted message by ID."""
        message = session.get(EncryptedContent, message_id)
        if message:
            try:
                if message.burn_after_reading:
                    session.delete(message)
                    session.commit()
                return EncryptedContent.model_validate(message)
            except Exception:
                session.rollback()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="An error occurred while deleting the message after reading.",
                )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorMessages.MESSAGE_NOT_FOUND,
        )

    @staticmethod
    async def delete_message(message_id: str, session: Session) -> EncryptedContent:
        """Delete an encrypted message by ID."""
        message = session.get(EncryptedContent, message_id)

        try:
            if not message:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=ErrorMessages.MESSAGE_NOT_FOUND,
                )
            deleted_message = EncryptedContent.model_validate(message)
            session.delete(message)
            session.commit()
            return deleted_message

        except Exception:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.DELETE_ERROR,
            )

    @staticmethod
    async def delete_message(message_id: str, session: Session) -> EncryptedContent:
        """Delete an encrypted message by ID."""
        message = session.get(EncryptedContent, message_id)
        if not message:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=ErrorMessages.MESSAGE_NOT_FOUND,
            )
        try:

            deleted_message = EncryptedContent.model_validate(message)
            session.delete(message)
            session.commit()
            return deleted_message

        except Exception:
            session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.DELETE_ERROR,
            )
