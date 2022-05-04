from data.type_aliases import TranslateFunc
from aiogram.types import Message

from services.keyboards import build_main_menu


async def handler(message: Message, translate: TranslateFunc):
    # TODO: Set user state to 'free'
    await message.answer(
        translate('error_unknown_command'),
        reply_markup=build_main_menu(
            translate,
            True,  # TODO: Use real user data
        ),
    )
