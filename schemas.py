from pydantic import BaseModel
from typing import Optional

class ShowResponse(BaseModel):
    id: int
    title: str
    year: str
    genre: str
    plot: str
    imdb_rating: Optional[float]
    imdb_id: str

    class Config:
        from_attributes = True