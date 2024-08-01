from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
from movie_service.app.api.models import MovieIn, MovieOut
from movie_service.app.api import db_manager


# fake_movie_db = [
#     {
#         'name': 'Star War: Episode IX - The Rise of SkyWalker',
#         'plot': 'The Surviving member of the resistance face the First Order again',
#         'genres': ['Action', 'Adventure', 'Fantasy', 'Sci-fi'],
#         'casts': ['Daisy Ridley', 'Adam Driver']
#     }
# ]

movies: APIRouter = APIRouter()


@movies.get('/', response_model=List[MovieOut])
async def get_movies():
    return await db_manager.get_all_movies()


@movies.get('/{id}/', response_model=MovieOut)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie does not exist")

    return movie


@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    movie_id = await db_manager.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }
    return response


@movies.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie Not Found")

    update_data = payload.dict(exclude_unset=True)
    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update = update_data)

    return await db_manager.update_movie(id, updated_movie)


@movies.delete('/{id}')
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie Not Found")

    return await db_manager.delete_movie(id)
