from fastapi import status


def test_encrypt_message(client, session, encrypted_content):
    response = client.post("/encrypt", json=encrypted_content.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["message"] == encrypted_content.message
    assert data["iv"] == encrypted_content.iv


def test_encrypt_message_invalid_format(client, session):
    invalid_content = {
        "message": "invalid_base64_message",
        "iv": "test_iv"
    }
    response = client.post("/encrypt", json=invalid_content)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Invalid message format, expected base64 format"


def test_encrypt_message_empty_content(client, session):
    empty_content = {
        "message": "",
        "iv": "test_iv"
    }
    response = client.post("/encrypt", json=empty_content)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Message cannot be empty"
