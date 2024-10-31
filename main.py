from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apis.endpoints import router

app = FastAPI(
    title="Movies API",
    description=(
        "This API provides access to movie data, allowing you to list all movies, "
        "filter movies by genre, year, director, and other criteria. "
        "Use the endpoints to interact with the movie dataset."
    ),
    version="1.0.0",
    contact={
        "name": "Rahul Bhoyar",
        "email": "rahulbhoyaroffice@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Include the router
app.include_router(router, prefix="/api")

@app.get("/", include_in_schema=False)
async def root():
    """
    Redirects the root URL to the Swagger UI documentation.

    Returns:
        RedirectResponse: A response object that redirects to the '/docs' URL.
    """
    try:
        return RedirectResponse(url="/docs")
    except Exception as e:
        # Log the exception or handle it as needed
        raise RuntimeError("Failed to redirect to the documentation.") from e