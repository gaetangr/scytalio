from fastapi import HTTPException, status
from sqlmodel import Session
from models import EncryptedContent
from sqlalchemy.exc import IntegrityError


class MessageService:
    """Business logic for message handling"""

    @staticmethod
    async def create_message(
        content: EncryptedContent, session: Session
    ) -> EncryptedContent:
        """
        Create a new encrypted message.

        Args:
            content (EncryptedContent): The encrypted message content.
            session (Session): The database session.

        Returns:
            EncryptedContent: The stored encrypted message content.

        Raises:
            HTTPException: If the message format is invalid or message creation fails.
        """
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
                detail="Message creation failed due to integrity error",
            )

    @staticmethod
    async def get_message(message_id: str, session: Session) -> EncryptedContent:
        """
        Retrieve an encrypted message by ID.

        Args:
            message_id (str): The ID of the encrypted message.
            session (Session): The database session.

        Returns:
            EncryptedContent: The retrieved encrypted message content.

        Raises:
            HTTPException: If the message is not found or an error occurs during deletion.
        """
        message = session.get(EncryptedContent, message_id)
        if message:
            try:
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
            status_code=status.HTTP_404_NOT_FOUND, detail="Message not found"
        )
