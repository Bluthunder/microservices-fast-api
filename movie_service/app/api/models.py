from typing import Optional, List

from pydantic import BaseModel


class MovieIn(BaseModel):
    name: str
    plot: str
    genres: list[str]
    casts: list[str]
    id: int


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts: Optional[List[str]] = None
