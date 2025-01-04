import uuid

def test_encrypt_endpoint(client):
    response = client.post("/encrypt", json={"message": "test", "iv": "test"})
    assert response.status_code == 201

def test_decrypt_endpoint_with_non_uuid(client):
    response = client.get("/decrypt/1/")
    assert response.status_code == 400

def test_decrypt_endpoint_with_valid_uuid(client):
    valid_uuid = str(uuid.uuid4())
    response = client.get(f"/decrypt/{valid_uuid}/")
    assert response.status_code == 404
