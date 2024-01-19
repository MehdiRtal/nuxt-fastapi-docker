from alembic import context
from sqlmodel import SQLModel
import asyncio

from db import engine
from config import settings


target_metadata = SQLModel.metadata

def run_migrations_offline() :
    context.configure(url=str(settings.DB_URL), target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
