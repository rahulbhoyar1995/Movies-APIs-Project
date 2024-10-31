from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

# Test for the root endpoint that redirects to /docs
def test_root_redirect():
    response = client.get("/")
    assert response.status_code == 200
    assert str(response.url).endswith("/docs")