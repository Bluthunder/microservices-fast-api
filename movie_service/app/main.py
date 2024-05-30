from fastapi import FastAPI

from movie_service.app.api.movies import movies

app = FastAPI()

app.include_router(movies)