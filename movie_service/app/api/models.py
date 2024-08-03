from typing import Optional, List

from pydantic import BaseModel


class MovieIn(BaseModel):
    name: str
    plot: str
    genres: list[str]
    casts_id: list[int]
    id: int


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts_id: Optional[List[int]] = None
