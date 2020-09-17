from typing import Generator, Optional

import asyncpg
from aiohttp import web

from . import models


async def init_db(app: web.Application) -> Generator[None, None, None]:
    sub_app = app._subapps[0]  # Connexion adds a subapp
    sub_app["db"] = await asyncpg.create_pool(app["config"]["DB_URL"])
    yield
    await sub_app["db"].close()


async def get_booking_by_id(pool, *, booking_id: int) -> Optional[models.Booking]:
    row = await pool.fetchrow(
        "SELECT * FROM booking WHERE id = $1", booking_id
    )
    if row is not None:
        return models.Booking(**row)


async def create_booking(
    pool, *, booking_id: int, name: str, is_active: bool
) -> models.Booking:
    row = await pool.fetchrow(
        "INSERT INTO booking (id, name, is_active) VALUES ($1, $2, $3) RETURNING *",
        booking_id,
        name,
        is_active,
    )
    return models.Booking(**row)
