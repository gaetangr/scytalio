class ErrorMessages:
    EMPTY_MESSAGE = "Message cannot be empty"
    INTEGRITY_ERROR = "Message creation failed due to integrity error"
    MESSAGE_NOT_FOUND = "Message not found"
    DELETE_ERROR = "An error occurred while deleting the message after reading"


class APIEndpoints:
    DECRYPT_MESSAGE = "/decrypt/{message_id}"
    ENCRYPT_MESSAGE = "/encrypt"
    DELETE_MESSAGE = "/delete/{message_id}"
