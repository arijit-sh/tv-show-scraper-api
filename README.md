# TV Show Scraper API

🔗 **Live API:** https://tv-show-scraper-api.onrender.com/docs

A backend service that fetches real TV show data from the OMDb API, stores it in a PostgreSQL database, and serves it through a custom-built REST API.

## Features

- Scrape and save a single show by title
- Batch scrape multiple shows in one request
- View all saved shows or look up one by ID
- Delete a saved show
- Data pulled live from OMDb (IMDb ratings, genre, plot, year, etc.) and persisted in Postgres

## Tech Stack

- **Python**
- **FastAPI** — web framework
- **SQLAlchemy** — database ORM
- **PostgreSQL (Neon)** — database
- **Requests** — external API calls
- **python-dotenv** — environment variable management

## Endpoints

| Method | Endpoint              | Description                          |
|--------|------------------------|----------------------------------------|
| GET    | `/`                    | Health check                          |
| POST   | `/shows/batch`         | Scrape and save multiple shows        |
| POST   | `/shows/{title}`       | Scrape and save a single show         |
| GET    | `/shows`               | Get all saved shows                   |
| GET    | `/shows/{show_id}`     | Get a single saved show by ID         |
| DELETE | `/shows/{show_id}`     | Delete a saved show                   |

## Running Locally

1. Clone the repo

git clone https://github.com/arijit-sh/tv-show-scraper-api.git
cd tv-show-scraper-api

2. Create and activate a virtual environment

py -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Create a `.env` file in the root folder with your own OMDb API key:

OMDB_API_KEY=your_key_here

Get a free key at [omdbapi.com](https://www.omdbapi.com/apikey.aspx)

5. Run the server

uvicorn main:app --reload

6. Open `http://127.0.0.1:8000/docs` to test the API interactively

## What I Learned

Built this project to practice working with external APIs, not just my own database. Key takeaways: FastAPI route-ordering bugs (exact-path routes must be defined before wildcard `{param}` routes, or the wildcard swallows everything), safely handling API keys with environment variables, transforming third-party API data into my own database schema, and deploying with a different database provider (Neon) than my primary host (Render).