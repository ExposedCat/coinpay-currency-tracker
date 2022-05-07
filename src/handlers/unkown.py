from data.type_aliases import TranslateFunc
from aiogram.types import Message
from entities.user import User

from services.keyboards import build_main_menu


async def handler(message: Message, translate: TranslateFunc, user: User):
    await user.update({'state': 'free'})
    await message.answer(
        translate('error_unknown_command'),
        reply_markup=build_main_menu(
            translate,
            user.get('notifications_enabled'),
        ),
    )
