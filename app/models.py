from datetime import datetime
from typing import Optional
import uuid
from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


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
    burn_after_reading: bool = Field(
        description="Default to true, can be read only once and then it is deleted.",
        default=True,
    )
    hmac: str = Field(
        description="A hash-based message authentication code (HMAC) derived from the UUID and AES key stored on the client side. It is used to authorize requests."
    )

    model_config = ConfigDict(from_attributes=True, extra="allow")


class WebsiteStats(SQLModel, table=True):
    """Track website statistics with single instance pattern"""

    id: str = Field(default="global_stats", primary_key=True)
    total_links_generated: int = Field(
        default=0, description="Total number of links created"
    )
    last_link_generated: Optional[datetime] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)
