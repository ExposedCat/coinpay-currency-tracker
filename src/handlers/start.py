from data.type_aliases import TranslateFunc
from aiogram import types
from entities.user import User

from services.keyboards import build_main_menu


async def handler(message: types.Message, translate: TranslateFunc, user: User):
    name = message.from_user.full_name
    await message.answer(
        translate('start', {'name': name}),
        reply_markup=build_main_menu(
            translate,
            user.get('notifications_enabled'),
        ),
    )
