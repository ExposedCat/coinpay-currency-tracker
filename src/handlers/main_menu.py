from data.type_aliases import TranslateFunc
from aiogram.types import Message
from entities.user import User

from services.keyboards import build_main_menu


async def handler(message: Message, translate: TranslateFunc, user: User):
    # TODO: Set user state to 'free'
    await message.answer(
        translate('main_menu'),
        reply_markup=build_main_menu(
            translate,
            True,  # TODO: Use real user data
        ),
    )
