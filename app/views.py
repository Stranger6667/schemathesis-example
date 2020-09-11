from aiohttp import web

from . import db


async def get_booking_by_id(request: web.Request, booking_id: int) -> web.Response:
    booking = await db.get_booking_by_id(request.app["db"], booking_id=booking_id)
    if booking is not None:
        data = booking.asdict()
    else:
        data = {}
    return web.json_response(data)


async def create_booking(request: web.Request, body) -> web.Response:
    booking = await db.create_booking(
        request.app["db"],
        booking_id=body["id"],
        name=body["name"],
        is_active=body["is_active"],
    )
    return web.json_response(booking.asdict())
