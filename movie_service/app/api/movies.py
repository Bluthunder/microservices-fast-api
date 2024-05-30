from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
from movie_service.app.api.models import Movie


fake_movie_db = [
    {
        'name': 'Star War: Episode IX - The Rise of SkyWalker',
        'plot': 'The Surviving member of the resistance face the First Order again',
        'genres': ['Action', 'Adventure', 'Fantasy', 'Sci-fi'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]

movies: APIRouter = APIRouter()


@movies.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db


@movies.post('/', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.model_dump()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}


@movies.put('/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.model_dump()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return f'Movie with {id} is updated'

    raise HTTPException(status_code=404, detail='Movie with given id does not exist')


@movies.delete('/{id}')
async def delete_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        del fake_movie_db[id]
        return f'Movie with {id} deleted'
    raise HTTPException(status_code=404, detail='Movie with given id does not exist')
