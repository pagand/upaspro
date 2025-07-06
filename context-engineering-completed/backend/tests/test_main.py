
from fastapi.testclient import TestClient
from unittest.mock import patch
from backend.app.main import app

client = TestClient(app)

@patch('backend.app.services.gemini_service.get_gemini_response')
def test_query_endpoint(mock_get_gemini_response):
    mock_get_gemini_response.return_value = "This is a test response."
    response = client.post("/query", json={"query": "test query"})
    assert response.status_code == 200
    assert response.json() == {"response": "This is a test response."}
