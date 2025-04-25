import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app
from app.services.llm_client import LLMClient

client = TestClient(app)

def test_ask_endpoint_success():
    # Mock the LLM response
    with patch.object(LLMClient, 'get_response', return_value="Mocked answer"):
        response = client.post("/api/ask", json={"question": "What is the meaning of life?"})
        assert response.status_code == 200
        assert response.json() == {"answer": "Mocked answer"}

def test_ask_endpoint_validation_error():
    # Test with missing question field
    response = client.post("/api/ask", json={})
    assert response.status_code == 422  # Validation error

def test_ask_endpoint_server_error():
    # Mock an exception in the LLM client
    with patch.object(LLMClient, 'get_response', side_effect=Exception("Test error")):
        response = client.post("/api/ask", json={"question": "What is the meaning of life?"})
        assert response.status_code == 500
        assert "LLM error" in response.json()["detail"] 