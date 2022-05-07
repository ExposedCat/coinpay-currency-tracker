from data.type_aliases import TranslateFunc
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup
from entities.user import User


async def handler(call: CallbackQuery, translate: TranslateFunc, user: User):
async def handler(call: CallbackQuery, translate: TranslateFunc):
    # TODO: Set user state to 'input_interval'
    # TODO: Set user pair in db
    pair = call.data.split('_', 1)[1]
    await call.message.edit_text(
        translate('input_interval'),
        reply_markup=ReplyKeyboardMarkup(),
    )
