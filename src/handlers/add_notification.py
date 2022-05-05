from locale import currency
from data.type_aliases import TranslateFunc
from aiogram.types import Message

from services.api import get_currencies
from services.keyboards import build_currencies_keyboard


async def handler(message: Message, translate: TranslateFunc):
    # TODO: Set user state to 'free'
    currencies = await get_currencies()
    await message.answer(
        translate('choose_to_buy'),
        reply_markup=build_currencies_keyboard(currencies),
    )
