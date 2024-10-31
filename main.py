# main_dir/main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apis.endpoints import router

app = FastAPI(
    title="Movies API",
    description="""
    This API provides access to movie data, allowing you to list all movies, filter movies by genre, year, director, and other criteria.
    Use the endpoints to interact with the movie dataset.
    """,
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

# Sample root endpoint to redirect to Swagger UI
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
