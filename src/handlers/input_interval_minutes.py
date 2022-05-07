from data.type_aliases import TranslateFunc
from aiogram.types import Message
from entities.user import User
from services.db_subscriptions import SubscriptionsMgr

from services.keyboards import build_main_menu


async def handler(
    message: Message,
    translate: TranslateFunc,
    user: User,
    subscriptions_mgr: SubscriptionsMgr,
):
    if message.text.isdigit():
        await subscriptions_mgr.update_or_create(
            user.get('pair'),
            user.get('interval') + int(message.text),
            user.get('id'),
        )
        await user.update(
            {
                'state': 'free',
                'interval': 0,
            }
        )
        await message.answer(
            translate('notification_added'),
            reply_markup=build_main_menu(translate, user.get('notifications_enabled')),
        )
    else:
        await message.answer(translate('error_not_a_number'))
