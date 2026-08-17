from sqlalchemy import Column, Integer, String, Float
from database import Base

class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    year = Column(String)
    genre = Column(String)
    plot = Column(String)
    imdb_rating = Column(Float, nullable=True)
    imdb_id = Column(String, unique=True)