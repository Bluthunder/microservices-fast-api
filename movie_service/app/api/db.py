from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://postgres:pass123@localhost:5432/movie_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movie_details',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('plot', String),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URL)