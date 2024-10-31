import pandas as pd
from fastapi import APIRouter, HTTPException
from models.genre import GenreInput, MoviesOutput

router = APIRouter()

# Load the data
data = pd.read_csv("./data/imdb_data.csv")

@router.get("/movies", response_model=MoviesOutput)
async def list_all_movies():
    movies = list(data["name"])
    return MoviesOutput(movies=movies)

# 1. Get movies by year
@router.get("/movies/by_year/{year}")
async def get_movies_by_year(year: int):
    movies = data[data["year"] == year]["name"].tolist()
    return {"year": year, "movies": movies}

# 2. Get movie by rank
@router.get("/movie/by_rank/{rank}")
async def get_movie_by_rank(rank: int):
    movie = data[data["rank"] == rank]["name"].values
    return {"rank": rank, "movie": movie[0]} if len(movie) > 0 else {"error": "Rank not found"}

# 3. Get top N movies by rating
@router.get("/movies/top_rated/{n}")
async def get_top_rated_movies(n: int):
    top_movies = data.nlargest(n, "rating")[["name", "rating"]]
    return {"top_rated_movies": top_movies.to_dict(orient="records")}

# 4. Get movies by certificate
@router.get("/movies/by_certificate/{certificate}")
async def get_movies_by_certificate(certificate: str):
    movies = data[data["certificate"] == certificate]["name"].tolist()
    return {"certificate": certificate, "movies": movies}

# 5. Get movies by runtime less than specified time (in minutes)
@router.get("/movies/shorter_than/{minutes}")
async def get_movies_shorter_than(minutes: int):
    movies = data[data["run_time"] <= minutes]["name"].tolist()
    return {"max_runtime": minutes, "movies": movies}

# 6. Get movies with a specific director
@router.get("/movies/by_director/{director}")
async def get_movies_by_director(director: str):
    movies = data[data["directors"].str.contains(director, case=False, na=False)]["name"].tolist()
    return {"director": director, "movies": movies}

# 7. Get movies with a specific writer
@router.get("/movies/by_writer/{writer}")
async def get_movies_by_writer(writer: str):
    movies = data[data["writers"].str.contains(writer, case=False, na=False)]["name"].tolist()
    return {"writer": writer, "movies": movies}

# 8. Get movies released between two years
@router.get("/movies/between_years")
async def get_movies_between_years(start_year: int, end_year: int):
    movies = data[(data["year"] >= start_year) & (data["year"] <= end_year)]["name"].tolist()
    return {"start_year": start_year, "end_year": end_year, "movies": movies}

# 9. Get movies by cast member
@router.get("/movies/by_cast/{cast_member}")
async def get_movies_by_cast(cast_member: str):
    movies = data[data["casts"].str.contains(cast_member, case=False, na=False)]["name"].tolist()
    return {"cast_member": cast_member, "movies": movies}

# 10. Get movies by tagline keyword
@router.get("/movies/by_tagline_keyword/{keyword}")
async def get_movies_by_tagline_keyword(keyword: str):
    movies = data[data["tagline"].str.contains(keyword, case=False, na=False)]["name"].tolist()
    return {"keyword": keyword, "movies": movies}

# 11. Get movies with a budget greater than a specified amount
@router.get("/movies/budget_greater_than/{budget}")
async def get_movies_budget_greater_than(budget: float):
    movies = data[data["budget"] >= budget]["name"].tolist()
    return {"min_budget": budget, "movies": movies}

# 12. Get movies with a box office collection greater than a specified amount
@router.get("/movies/box_office_greater_than/{box_office}")
async def get_movies_box_office_greater_than(box_office: float):
    movies = data[data["box_office"] >= box_office]["name"].tolist()
    return {"min_box_office": box_office, "movies": movies}

# 13. Get all distinct genres in the dataset
@router.get("/movies/genres")
async def get_all_genres():
    genres = data["genre"].dropna().unique().tolist()
    return {"genres": genres}

# 14. Get average rating for a specific genre
@router.get("/movies/average_rating/{genre}")
async def get_average_rating_for_genre(genre: str):
    genre_data = data[data["genre"] == genre]
    if not genre_data.empty:
        avg_rating = genre_data["rating"].mean()
        return {"genre": genre, "average_rating": avg_rating}
    else:
        raise HTTPException(status_code=404, detail="Genre not found")

# 15. Get highest box office movie by year
@router.get("/movies/highest_box_office/{year}")
async def get_highest_box_office_movie_by_year(year: int):
    year_data = data[data["year"] == year]
    if not year_data.empty:
        highest_box_office_movie = year_data.loc[year_data["box_office"].idxmax()][["name", "box_office"]]
        return {"year": year, "highest_box_office_movie": highest_box_office_movie.to_dict()}
    else:
        raise HTTPException(status_code=404, detail="Year not found")
