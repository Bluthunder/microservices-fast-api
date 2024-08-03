from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)

from databases import Database

import os

# DATABASE_URL = 'postgresql://postgres:pass123@localhost:5432/movie_db'
DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movie_details',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('plot', String),
    Column('genres', ARRAY(String)),
    Column('casts_id', ARRAY(Integer))
)

database = Database(DATABASE_URI)