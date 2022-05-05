from data.type_aliases import TranslateFunc
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup

from services.api import get_pair
from services.keyboards import build_pairs_keyboard


async def handler(call: CallbackQuery, translate: TranslateFunc):
    # TODO: Set user state to 'input_interval'
    # TODO: Set user pair in db
    pair = call.data.split('_', 1)[1]
    print(pair)
    await call.message.edit_text(
        translate('input_interval'),
        reply_markup=ReplyKeyboardMarkup(),
    )
