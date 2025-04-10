from sqlalchemy import create_engine, pool
from app.db import Base

from base_settings import get_settings


settings = get_settings()


def get_sync_engine():
    return create_engine(
        settings.DATABASE_URL.replace("+asyncpg", ""), poolclass=pool.NullPool
    )


def get_metadata():
    return Base.metadata
