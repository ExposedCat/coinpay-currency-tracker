from data.type_aliases import TranslateFunc
from aiogram import types

from services.keyboards import build_main_menu


async def handler(
    message: types.Message,
    translate: TranslateFunc,
):
    name = message.from_user.full_name
    await message.reply(
        translate('start', {'name': name}),
        # TODO: Check whether user has notifications enabled or not
        reply_markup=build_main_menu(translate, False),
    )
