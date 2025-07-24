from pydantic import BaseModel, Field, constr
from typing import Optional

class BoardGameCreate(BaseModel):
    id: Optional[int] = None
    name: constr(min_length=1)
    publisher: constr(min_length=1)
    year: int = Field(..., ge=1900, le=2025)
    rating: float = Field(..., ge=0.0, le=10.0)
    genre: Optional[str] = None
