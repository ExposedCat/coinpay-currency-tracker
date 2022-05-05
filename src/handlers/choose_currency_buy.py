from data.type_aliases import TranslateFunc
from aiogram.types import CallbackQuery

from services.api import get_pair
from services.keyboards import build_pairs_keyboard


async def handler(call: CallbackQuery, translate: TranslateFunc):
    currency = call.data.split('_')[1]
    pairs = await get_pair(currency)
    await call.message.edit_text(
        translate('choose_to_sell'),
        reply_markup=build_pairs_keyboard(currency, pairs),
    )
