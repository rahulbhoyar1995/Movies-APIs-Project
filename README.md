# Movies-APIs-Project

### Author : Rahul Bhoyar

Welcome to the Movies-APIs-Project!


This is a FastAPI application that provides various endpoints to interact with movie data sourced from an IMDb dataset. The application allows users to retrieve movie information based on different criteria.

## Directory Structure

```
Movies-APIs-Project/
├── apis/
│   ├── __init__.py
│   └── endpoints.py
├── requirements.txt
├── tests/
│   ├── test_endpoints.py
│   └── test_main.py
├── models/
│   └── genre.py
├── README.md
├── .gitignore
├── main.py
└── data/
    └── imdb_data.csv
```

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rahulbhoyar1995/Movies-APIs-Project.git
   cd Movies-APIs-Project
   ```
2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI application:**

   ```bash
   uvicorn main:app --reload
   ```
2. **Access the API documentation:**
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the Swagger UI.

## Endpoints

The following endpoints are available:

1. **List all movies:**

   - **GET** `/api/movies`
   - Returns a list of all movie names.
2. **Get movies by year:**

   - **GET** `/api/movies/by_year/{year}`
   - Retrieves movies released in a specific year.
3. **Get movie by rank:**

   - **GET** `/api/movie/by_rank/{rank}`
   - Retrieves a movie based on its rank.
4. **Get top N movies by rating:**

   - **GET** `/api/movies/top_rated/{n}`
   - Returns the top N movies by rating.
5. **Get movies by certificate:**

   - **GET** `/api/movies/by_certificate/{certificate}`
   - Retrieves movies based on their certification.
6. **Get movies shorter than specified runtime:**

   - **GET** `/api/movies/shorter_than/{minutes}`
   - Retrieves movies with a runtime shorter than the specified minutes.
7. **Get movies by director:**

   - **GET** `/api/movies/by_director/{director}`
   - Retrieves movies directed by a specific director.
8. **Get movies by writer:**

   - **GET** `/api/movies/by_writer/{writer}`
   - Retrieves movies written by a specific writer.
9. **Get movies released between two years:**

   - **GET** `/api/movies/between_years`
   - Retrieves movies released between specified start and end years.
10. **Get movies by cast member:**

    - **GET** `/api/movies/by_cast/{cast_member}`
    - Retrieves movies featuring a specific cast member.
11. **Get movies by tagline keyword:**

    - **GET** `/api/movies/by_tagline_keyword/{keyword}`
    - Retrieves movies containing a specific keyword in their tagline.
12. **Get movies with a budget greater than a specified amount:**

    - **GET** `/api/movies/budget_greater_than/{budget}`
    - Retrieves movies with a budget exceeding the specified amount.
13. **Get movies with a box office collection greater than a specified amount:**

    - **GET** `/api/movies/box_office_greater_than/{box_office}`
    - Retrieves movies with box office collections exceeding the specified amount.
14. **Get all distinct genres in the dataset:**

    - **GET** `/api/movies/genres`
    - Retrieves a list of distinct genres present in the dataset.
15. **Get average rating for a specific genre:**

    - **GET** `/api/movies/average_rating/{genre}`
    - Retrieves the average rating for a specific genre.
16. **Get highest box office movie by year:**

    - **GET** `/api/movies/highest_box_office/{year}`
    - Retrieves the highest box office movie for a specific year.

## Testing

To run the test suite, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
