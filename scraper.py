import os
import requests
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import models

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")

def fetch_show_from_omdb(title: str):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "False":
        return None

    return data

def save_show_to_db(db: Session, show_data: dict):
    existing = db.query(models.Show).filter(models.Show.imdb_id == show_data["imdbID"]).first()
    if existing:
        return existing

    rating = show_data.get("imdbRating")
    try:
        rating = float(rating)
    except (TypeError, ValueError):
        rating = None

    new_show = models.Show(
        title=show_data.get("Title"),
        year=show_data.get("Year"),
        genre=show_data.get("Genre"),
        plot=show_data.get("Plot"),
        imdb_rating=rating,
        imdb_id=show_data.get("imdbID")
    )

    db.add(new_show)
    db.commit()
    db.refresh(new_show)
    return new_show 