from data.type_aliases import TranslateFunc
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup
from services.db_subscriptions import SubscriptionsMgr


async def handler(
    call: CallbackQuery,
    translate: TranslateFunc,
    subscriptions_mgr: SubscriptionsMgr,
):
    subscription_id = call.data.split('_')[2]
    await subscriptions_mgr.delete(subscription_id)
    await call.message.edit_text(
        translate('notification_deleted'),
        reply_markup=ReplyKeyboardMarkup(),
    )
