# main_dir/api/models.py
from pydantic import BaseModel
from typing import List

class GenreInput(BaseModel):
    genre: str

class MoviesOutput(BaseModel):
    movies: List[str]
