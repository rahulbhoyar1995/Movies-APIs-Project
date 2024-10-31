from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

def test_root_redirect():
    """
    Test the root endpoint to ensure it redirects to the /docs endpoint.

    This function sends a GET request to the root endpoint ("/") and checks
    if the response status code is 200 and the URL ends with "/docs".

    Raises:
        AssertionError: If the response status code is not 200 or the URL
                        does not end with "/docs".
    """
    try:
        response = client.get("/")
        assert response.status_code == 200, "Expected status code 200"
        assert str(response.url).endswith("/docs"), "Expected URL to end with '/docs'"
    except AssertionError as e:
        print(f"Test failed: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise