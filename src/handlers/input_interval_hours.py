from data.type_aliases import TranslateFunc
from aiogram.types import Message
from entities.user import User
from services.db_subscriptions import SubscriptionsMgr

from services.keyboards import build_main_menu


async def handler(message: Message, translate: TranslateFunc, user: User):
    if message.text.isdigit():
        hours = int(message.text)
        await user.update(
            {
                'state': 'input_interval_minutes',
                'interval': hours * 60,
            }
        )
        await message.answer(
            translate('input_interval_minutes'),
            reply_markup=build_main_menu(
                translate, user.get('notifications_enabled')
            ),
        )
    else:
        await message.answer(translate('error_not_a_number'))
