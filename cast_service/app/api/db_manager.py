from cast_service.app.api.models import CastIn, CastOut, CastUpdate
from cast_service.app.api.db import casts, databases


async def add_cast(payload: CastIn):
    query = casts.insert().values(**payload.dict())

    return await databases.execute(query=query)


async def get_cast(id):
    query = casts.select(casts.c.id == id)
    return await databases.fetch_one(query=query)
