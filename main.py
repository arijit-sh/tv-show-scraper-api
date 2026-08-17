from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import scraper
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "TV Show Scraper API is alive"}

@app.post("/shows/batch", response_model=list[schemas.ShowResponse])
def scrape_multiple_shows(titles: list[str], db: Session = Depends(get_db)):
    results = []
    for title in titles:
        show_data = scraper.fetch_show_from_omdb(title)
        if show_data is not None:
            saved_show = scraper.save_show_to_db(db, show_data)
            results.append(saved_show)
    return results

@app.post("/shows/{title}", response_model=schemas.ShowResponse)
def scrape_and_save_show(title: str, db: Session = Depends(get_db)):
    show_data = scraper.fetch_show_from_omdb(title)

    if show_data is None:
        raise HTTPException(status_code=404, detail=f"Show '{title}' not found on OMDb")

    saved_show = scraper.save_show_to_db(db, show_data)
    return saved_show

@app.get("/shows", response_model=list[schemas.ShowResponse])
def get_all_shows(db: Session = Depends(get_db)):
    return db.query(models.Show).all()

@app.get("/shows/{show_id}", response_model=schemas.ShowResponse)
def get_show(show_id: int, db: Session = Depends(get_db)):
    show = db.query(models.Show).filter(models.Show.id == show_id).first()
    if not show:
        raise HTTPException(status_code=404, detail="Show not found")
    return show

@app.delete("/shows/{show_id}")
def delete_show(show_id: int, db: Session = Depends(get_db)):
    show = db.query(models.Show).filter(models.Show.id == show_id).first()
    if not show:
        raise HTTPException(status_code=404, detail="Show not found")
    db.delete(show)
    db.commit()
    return {"message": "Show deleted"}