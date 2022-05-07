from data.type_aliases import TranslateFunc
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup
from entities.user import User


async def handler(call: CallbackQuery, translate: TranslateFunc, user: User):
    pair = call.data.split('_', 1)[1]
    await user.update(
        {
            'state': 'input_interval',
            'pair': pair,
        }
    )
    await call.message.edit_text(
        translate('input_interval'),
        reply_markup=ReplyKeyboardMarkup(),
    )
