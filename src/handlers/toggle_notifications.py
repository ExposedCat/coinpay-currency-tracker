from data.type_aliases import TranslateFunc
from aiogram.types import Message
from entities.user import User

from services.keyboards import build_main_menu


async def handler_on(message: Message, translate: TranslateFunc, user: User):
    await user.update({'notifications_enabled': True})
    await message.answer(
        translate('notifications_enabled'),
        reply_markup=build_main_menu(translate, True),
    )


async def handler_off(message: Message, translate: TranslateFunc, user: User):
    await user.update({'notifications_enabled': False})
    await message.answer(
        translate('notifications_disabled'),
        reply_markup=build_main_menu(translate, False),
    )
