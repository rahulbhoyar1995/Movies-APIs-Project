import pandas as pd
from fastapi import APIRouter, HTTPException
from models.genre import GenreInput, MoviesOutput

router = APIRouter()

# Load the data
try:
    data = pd.read_csv("./data/imdb_data.csv")
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Data file not found")
except pd.errors.EmptyDataError:
    raise HTTPException(status_code=500, detail="Data file is empty")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/movies", response_model=MoviesOutput)
async def list_all_movies():
    """
    List all movies in the dataset.

    Returns:
        MoviesOutput: A list of all movie names.
    """
    movies = list(data["name"])
    return MoviesOutput(movies=movies)

@router.get("/movies/by_year/{year}")
async def get_movies_by_year(year: int):
    """
    Get movies released in a specific year.

    Args:
        year (int): The year to filter movies by.

    Returns:
        dict: A dictionary containing the year and a list of movie names.
    """
    movies = data[data["year"] == year]["name"].tolist()
    return {"year": year, "movies": movies}

@router.get("/movie/by_rank/{rank}")
async def get_movie_by_rank(rank: int):
    """
    Get a movie by its rank.

    Args:
        rank (int): The rank of the movie.

    Returns:
        dict: A dictionary containing the rank and the movie name, or an error message if not found.
    """
    movie = data[data["rank"] == rank]["name"].values
    return {"rank": rank, "movie": movie[0]} if len(movie) > 0 else {"error": "Rank not found"}

@router.get("/movies/top_rated/{n}")
async def get_top_rated_movies(n: int):
    """
    Get the top N movies by rating.

    Args:
        n (int): The number of top-rated movies to retrieve.

    Returns:
        dict: A dictionary containing a list of top-rated movies with their ratings.
    """
    top_movies = data.nlargest(n, "rating")[["name", "rating"]]
    return {"top_rated_movies": top_movies.to_dict(orient="records")}

@router.get("/movies/by_certificate/{certificate}")
async def get_movies_by_certificate(certificate: str):
    """
    Get movies by certificate.

    Args:
        certificate (str): The certificate to filter movies by.

    Returns:
        dict: A dictionary containing the certificate and a list of movie names.
    """
    movies = data[data["certificate"] == certificate]["name"].tolist()
    return {"certificate": certificate, "movies": movies}

@router.get("/movies/shorter_than/{minutes}")
async def get_movies_shorter_than(minutes: int):
    """
    Get movies with a runtime less than the specified time.

    Args:
        minutes (int): The maximum runtime in minutes.

    Returns:
        dict: A dictionary containing the maximum runtime and a list of movie names.
    """
    movies = data[data["run_time"] <= minutes]["name"].tolist()
    return {"max_runtime": minutes, "movies": movies}

@router.get("/movies/by_director/{director}")
async def get_movies_by_director(director: str):
    """
    Get movies by a specific director.

    Args:
        director (str): The director's name to filter movies by.

    Returns:
        dict: A dictionary containing the director's name and a list of movie names.
    """
    movies = data[data["directors"].str.contains(director, case=False, na=False)]["name"].tolist()
    return {"director": director, "movies": movies}

@router.get("/movies/by_writer/{writer}")
async def get_movies_by_writer(writer: str):
    """
    Get movies by a specific writer.

    Args:
        writer (str): The writer's name to filter movies by.

    Returns:
        dict: A dictionary containing the writer's name and a list of movie names.
    """
    movies = data[data["writers"].str.contains(writer, case=False, na=False)]["name"].tolist()
    return {"writer": writer, "movies": movies}

@router.get("/movies/between_years")
async def get_movies_between_years(start_year: int, end_year: int):
    """
    Get movies released between two years.

    Args:
        start_year (int): The start year.
        end_year (int): The end year.

    Returns:
        dict: A dictionary containing the start and end years and a list of movie names.
    """
    movies = data[(data["year"] >= start_year) & (data["year"] <= end_year)]["name"].tolist()
    return {"start_year": start_year, "end_year": end_year, "movies": movies}

@router.get("/movies/by_cast/{cast_member}")
async def get_movies_by_cast(cast_member: str):
    """
    Get movies by a specific cast member.

    Args:
        cast_member (str): The cast member's name to filter movies by.

    Returns:
        dict: A dictionary containing the cast member's name and a list of movie names.
    """
    movies = data[data["casts"].str.contains(cast_member, case=False, na=False)]["name"].tolist()
    return {"cast_member": cast_member, "movies": movies}

@router.get("/movies/by_tagline_keyword/{keyword}")
async def get_movies_by_tagline_keyword(keyword: str):
    """
    Get movies by a keyword in the tagline.

    Args:
        keyword (str): The keyword to filter movies by.

    Returns:
        dict: A dictionary containing the keyword and a list of movie names.
    """
    movies = data[data["tagline"].str.contains(keyword, case=False, na=False)]["name"].tolist()
    return {"keyword": keyword, "movies": movies}

@router.get("/movies/budget_greater_than/{budget}")
async def get_movies_budget_greater_than(budget: float):
    """
    Get movies with a budget greater than a specified amount.

    Args:
        budget (float): The minimum budget.

    Returns:
        dict: A dictionary containing the minimum budget and a list of movie names.
    """
    movies = data[data["budget"] >= budget]["name"].tolist()
    return {"min_budget": budget, "movies": movies}

@router.get("/movies/box_office_greater_than/{box_office}")
async def get_movies_box_office_greater_than(box_office: float):
    """
    Get movies with a box office collection greater than a specified amount.

    Args:
        box_office (float): The minimum box office collection.

    Returns:
        dict: A dictionary containing the minimum box office collection and a list of movie names.
    """
    movies = data[data["box_office"] >= box_office]["name"].tolist()
    return {"min_box_office": box_office, "movies": movies}

@router.get("/movies/genres")
async def get_all_genres():
    """
    Get all distinct genres in the dataset.

    Returns:
        dict: A dictionary containing a list of unique genres.
    """
    genres = data["genre"].dropna().unique().tolist()
    return {"genres": genres}

@router.get("/movies/average_rating/{genre}")
async def get_average_rating_for_genre(genre: str):
    """
    Get the average rating for a specific genre.

    Args:
        genre (str): The genre to calculate the average rating for.

    Returns:
        dict: A dictionary containing the genre and its average rating.
    """
    genre_data = data[data["genre"] == genre]
    if not genre_data.empty:
        avg_rating = genre_data["rating"].mean()
        return {"genre": genre, "average_rating": avg_rating}
    else:
        raise HTTPException(status_code=404, detail="Genre not found")

@router.get("/movies/highest_box_office/{year}")
async def get_highest_box_office_movie_by_year(year: int):
    """
    Get the highest box office movie by year.

    Args:
        year (int): The year to filter movies by.

    Returns:
        dict: A dictionary containing the year and the highest box office movie details.
    """
    year_data = data[data["year"] == year]
    if not year_data.empty:
        highest_box_office_movie = year_data.loc[year_data["box_office"].idxmax()][["name", "box_office"]]
        return {"year": year, "highest_box_office_movie": highest_box_office_movie.to_dict()}
    else:
        raise HTTPException(status_code=404, detail="Year not found")