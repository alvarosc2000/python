from db.database import Base
from sqlalchemy import Column, Integer, String, Float, CheckConstraint

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre = Column(String, nullable=True)

    __table_args__ = (
        CheckConstraint("year >= 1500 AND year <= 2050", name="year_range"),
        CheckConstraint("rating >= 0.0 AND rating <= 5.0", name="rating_range"),
    )
