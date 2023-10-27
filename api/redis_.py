from fastapi import Depends
from redis.asyncio import Redis as Redis_
from typing import Annotated

from config import settings


connection = Redis_.from_url(settings.REDIS_URL)

async def get_redis_session():
    async with connection.client() as session:
        yield session

Redis = Annotated[Redis_, Depends(get_redis_session)]
