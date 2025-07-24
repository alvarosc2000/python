from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from db.database import Base

class BoardGame(Base):
    __tablename__ = 'boardgame'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    publisher = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    genre = Column(String)


    __table_args__ = (
        CheckConstraint("year BETWEEN 1900 AND 2025", name="year_range"),
        CheckConstraint("rating BETWEEN 0.0 AND 10.0", name="rating_range"),
    )
