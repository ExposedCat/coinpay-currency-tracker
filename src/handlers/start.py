from data.type_aliases import TranslateFunc
from aiogram import types



async def handler(
    message: types.Message,
    translate: TranslateFunc,
):
    await message.reply(
        text('start', {
            'name': message.from_user.full_name
        })
    )
