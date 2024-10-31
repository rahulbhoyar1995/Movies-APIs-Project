import pytest
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

def test_list_all_movies():
    """
    Test the GET /api/movies endpoint to ensure it lists all movies.

    This function sends a GET request to the /api/movies endpoint and checks:
    - The response status code is 200.
    - The response contains a "movies" key.
    - The "movies" key is associated with a list.
    """
    try:
        response = client.get("/api/movies")
        assert response.status_code == 200
        assert "movies" in response.json()
        assert isinstance(response.json()["movies"], list)
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {e}")

# Uncomment and complete the following tests as needed

# def test_get_movies_by_genre_valid():
#     """
#     Test the GET /api/movies/by_genre endpoint with a valid genre.

#     This function sends a GET request with a valid genre and checks:
#     - The response status code is 200.
#     - The response contains a "movies" key.
#     - The "movies" key is associated with a list.
#     - Each movie name in the list is a string.
#     """
#     genre = "Action"
#     try:
#         response = client.get(f"/api/movies/by_genre?genre={genre}")
#         assert response.status_code == 200
#         assert "movies" in response.json()
#         assert isinstance(response.json()["movies"], list)
#         for movie in response.json()["movies"]:
#             assert isinstance(movie, str)
#     except Exception as e:
#         pytest.fail(f"Test failed due to unexpected error: {e}")

# def test_get_movies_by_genre_invalid():
#     """
#     Test the GET /api/movies/by_genre endpoint with an invalid genre.

#     This function sends a GET request with an invalid genre and checks:
#     - The response status code is 200.
#     - The response contains a "movies" key.
#     - The "movies" key is associated with an empty list.
#     """
#     genre = "NonExistentGenre"
#     try:
#         response = client.get(f"/api/movies/by_genre?genre={genre}")
#         assert response.status_code == 200
#         assert "movies" in response.json()
#         assert response.json()["movies"] == []
#     except Exception as e:
#         pytest.fail(f"Test failed due to unexpected error: {e}")

# def test_get_movies_by_year():
#     """
#     Test the GET /api/movies/by_year endpoint with a specific year.

#     This function sends a GET request with a specific year and checks:
#     - The response status code is 200.
#     - The response contains a "movies" key.
#     - The "movies" key is associated with a list.
#     - Each movie name in the list is a string.
#     """
#     year = 2020
#     try:
#         response = client.get(f"/api/movies/by_year?year={year}")
#         assert response.status_code == 200
#         assert "movies" in response.json()
#         assert isinstance(response.json()["movies"], list)
#         for movie in response.json()["movies"]:
#             assert isinstance(movie, str)
#     except Exception as e:
#         pytest.fail(f"Test failed due to unexpected error: {e}")

# @pytest.mark.parametrize("genre, expected_status", [
#     ("Action", 200),
#     ("Comedy", 200),
#     ("NonExistentGenre", 200),
# ])
# def test_post_movies_by_genre(genre, expected_status):
#     """
#     Test the POST /api/movies endpoint with various genres.

#     This function sends a POST request with different genres and checks:
#     - The response status code matches the expected status.
#     - The response contains a "movies" key.
#     - The "movies" key is associated with a list.
#     """
#     try:
#         response = client.post("/api/movies", json={"genre": genre})
#         assert response.status_code == expected_status
#         assert "movies" in response.json()
#         assert isinstance(response.json()["movies"], list)
#     except Exception as e:
#         pytest.fail(f"Test failed due to unexpected error: {e}")