def test_encrypt_endpoint(client):
    response = client.post("/encrypt", json={"message": "test", "iv": "test"})
    assert response.status_code == 201


def test_decrypt_endpoint_with_non_uuid(client):
    response = client.get("/decrypt/1/")
    assert response.status_code == 400


def test_encrypt_message(client, session, encrypted_content):
    response = client.post("/encrypt", json=encrypted_content.model_dump())
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == encrypted_content.message
    assert data["iv"] == encrypted_content.iv


def test_encrypt_message_invalid_format(client, session):
    invalid_content = {
        "message": "invalid_base64_message",
        "iv": "test_iv"
    }
    response = client.post("/encrypt", json=invalid_content)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid message format, expected base64 format"


def test_encrypt_message_empty_content(client, session):
    empty_content = {
        "message": "",
        "iv": "test_iv"
    }
    response = client.post("/encrypt", json=empty_content)
    assert response.status_code == 400
    assert response.json()["detail"] == "Message cannot be empty"


def test_decrypt_message(client, session, encrypted_content):
    # First, encrypt a message
    response = client.post("/encrypt", json=encrypted_content.model_dump())
    assert response.status_code == 201
    message_id = response.json()["id"]

    # Then, decrypt the message
    response = client.get(f"/decrypt/{message_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == encrypted_content.message
    assert data["iv"] == encrypted_content.iv


def test_decrypt_message_invalid_id(client):
    response = client.get("/decrypt/invalid_id")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid message ID format, UUID expected."


def test_decrypt_message_not_found(client):
    response = client.get("/decrypt/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
    assert response.json()["detail"] == "Message not found"
