from fastapi import status


def test_encrypt_message(client, session, encrypted_content):
    response = client.post("/encrypt", json=encrypted_content.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["message"] == encrypted_content.message
    assert data["iv"] == encrypted_content.iv
