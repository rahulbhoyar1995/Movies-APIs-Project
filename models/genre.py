# main_dir/api/models.py

from typing import List
from pydantic import BaseModel

class GenreInput(BaseModel):
    """
    A Pydantic model representing the input for a genre.

    Attributes:
        genre (str): The name of the genre.
    """
    genre: str

class MoviesOutput(BaseModel):
    """
    A Pydantic model representing the output for a list of movies.

    Attributes:
        movies (List[str]): A list of movie titles.
    """
    movies: List[str]