from typing import Callable
from aiogram import types


async def handler(message: types.Message, text: Callable) -> None:
    await message.reply(
        text('start', {
            'name': message.from_user.full_name
        })
    )
