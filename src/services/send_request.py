from functools import partial

from aiogram import Bot


async def send_request(path: str, method: str = 'get') -> dict:
    bot = Bot.get_current()
    session = await bot.get_session()  # aiohttp session to send HTTP requests

    request = partial(
        session.get if method == 'get' else session.post,
        path,
    )

    async with request() as response:
        return await response.json()
