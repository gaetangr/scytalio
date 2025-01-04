import uuid
from pydantic import ConfigDict
from sqlmodel import Field, SQLModel
from pydantic import ConfigDict
from sqlalchemy import Index, inspect


class EncryptedContent(SQLModel, table=True):
    """
    Database model representing encrypted content.

    This model is used to store encrypted messages and their corresponding
    initialization vector (IV) in the database. It leverages SQLModel to
    avoid code duplication with the Pydantic schema.

    Attributes:
        id (str): A unique identifier for the encrypted content,
                  generated using UUID. This is used in URLs and avoids
                  Insecure Direct Object Reference (IDOR) attacks.
        message (str): The encrypted message, stored in Base64 format.
                       The message is not decipherable without the appropriate
                       decryption key on the client side.
        iv (str): The initialization vector (IV) used during encryption.
                  It can be sent in clear text, ensuring that even identical
                  content will have different ciphertexts.

    Notes:
        - The `id` attribute is a UUID to prevent predictable or sequential
          identifiers, thus reducing the risk of unauthorized access to content.
          [IDOR](https://portswigger.net/web-security/access-control/idor).
        - The `message` is encrypted using a symmetric encryption algorithm,
          and its Base64 encoding ensures that binary data can be safely transmitted.
        - The `iv` is an essential cryptographic component to ensure the security
          of the encryption by introducing randomness. It helps prevent attacks
          like replay or pattern recognition by guaranteeing that identical plaintext
          messages result in different ciphertexts.

        Most of the logic is done on the frontend using the native Crypto library available in
        all recent browsers See [MDN Web Docs on Crypto](https://developer.mozilla.org/en-US/docs/Web/API/Crypto).
    """

    __tablename__ = "encryptedcontent"
    __table_args__ = {"extend_existing": True}
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        description="A unique identifier for the encrypted content, used in the URL.",
    )
    message: str = Field(
        index=True, description="The encrypted message content, encoded in Base64."
    )
    iv: str = Field(
        description="The initialization vector used for encryption, sent in clear."
    )

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def create_index(cls, engine):
        inspector = inspect(engine)
        indexes = [index['name'] for index in inspector.get_indexes(cls.__tablename__)]
        if 'ix_encryptedcontent_message' not in indexes:
            Index('ix_encryptedcontent_message', cls.message).create(bind=engine)
