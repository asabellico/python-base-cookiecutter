def test_api_docs(api_client):
    response = api_client.get("/")
    assert response.status_code == 200

def test_api_health(api_client):
    response = api_client.get("/health")
    assert response.status_code == 200