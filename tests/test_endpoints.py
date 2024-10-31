import pytest
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

# Test for the GET /api/movies endpoint that lists all movies
def test_list_all_movies():
    response = client.get("/api/movies")
    assert response.status_code == 200
    assert "movies" in response.json()  # Ensure the "movies" key is in response
    assert isinstance(response.json()["movies"], list)  # Ensure it's a list of movies

# # Test for the GET /api/movies/by_genre endpoint with a valid genre
# def test_get_movies_by_genre_valid():
#     genre = "Action"
#     response = client.get(f"/api/movies/by_genre?genre={genre}")
#     assert response.status_code == 200
#     assert "movies" in response.json()  # Ensure "movies" key is present
#     assert isinstance(response.json()["movies"], list)  # Should return a list
#     # Check if the genre filter applied correctly (optional, depends on your data)
#     for movie in response.json()["movies"]:
#         assert isinstance(movie, str)  # Ensure movie names are strings

# # Test for the GET /api/movies/by_genre endpoint with an invalid genre
# def test_get_movies_by_genre_invalid():
#     genre = "NonExistentGenre"
#     response = client.get(f"/api/movies/by_genre?genre={genre}")
#     assert response.status_code == 200
#     assert "movies" in response.json()  # Ensure "movies" key is present
#     assert response.json()["movies"] == []  # Expect an empty list for invalid genre

# # Test for any additional endpoints you have
# # For example, assuming you added an endpoint to filter by year

# # Test for a hypothetical /api/movies/by_year endpoint
# def test_get_movies_by_year():
#     year = 2020
#     response = client.get(f"/api/movies/by_year?year={year}")
#     assert response.status_code == 200
#     assert "movies" in response.json()
#     assert isinstance(response.json()["movies"], list)
#     for movie in response.json()["movies"]:
#         assert isinstance(movie, str)

# # Additional test cases for endpoints by director, rating, etc., could be similar

# # Example of testing a POST endpoint, assuming one exists in your `router.py`
# @pytest.mark.parametrize("genre, expected_status", [
#     ("Action", 200),
#     ("Comedy", 200),
#     ("NonExistentGenre", 200),
# ])
# def test_post_movies_by_genre(genre, expected_status):
#     response = client.post("/api/movies", json={"genre": genre})
#     assert response.status_code == expected_status
#     assert "movies" in response.json()
#     assert isinstance(response.json()["movies"], list)

