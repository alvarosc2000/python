from pydantic import BaseModel, Field, constr
from typing import Optional

class BookCreate(BaseModel):
    id: Optional[int] = None
    title: constr(min_length=1)
    author: constr(min_length=1)
    year: int = Field(..., ge=1500, le=2050)
    rating: float = Field(..., ge=0.0, le=5.0)
    genre: Optional[str] = None
