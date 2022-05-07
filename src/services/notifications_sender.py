from aiogram import Bot
from aiogram.utils.exceptions import Throttled
from services.db_users import UsersMgr
from services.db_subscriptions import SubscriptionsMgr

from services.get_text_builder import build_get_text_func
from services.api import fetch_rates
from datetime import datetime


async def _send_notification(
    bot: Bot, user_id: int, texts: dict, lang: str, pair: str, rate: float
):
    try:
        translate = build_get_text_func(texts, lang)
        buy, sell = pair.split('_')
        text = translate(
            'notification',
            {
                'buy': buy,
                'sell': sell,
                'rate': rate,
            },
        )
        await bot.send_message(user_id, text)
    except Throttled:
        pass


def time_passed(date: datetime, seconds: int) -> bool:
    if date is None:
        return True
    now = datetime.now()
    delta = now - date
    print(f'seconds left {delta.seconds}')
    return delta.total_seconds() >= seconds


async def process_subscription(
    subscription: dict, user_data: dict, rates: dict, texts: dict, bot: Bot
):
    pair = subscription['currencies']
    rate = rates[pair] if pair in rates else 0
    await _send_notification(
        bot,
        user_id=subscription['user_id'],
        lang=user_data['lang'],
        pair=pair,
        rate=rate,
        texts=texts,
    )


async def send_notifications(
    users_mgr: UsersMgr, subscriptions_mgr: SubscriptionsMgr, texts: dict
):
    bot = Bot.get_current()
    users = {}
    users_cursor = users_mgr.get_users()
    async for user in users_cursor:
        users[user['id']] = {
            'lang': user['lang'],
            'state': user['state'],
        }
    subscriptions = subscriptions_mgr.get_all()
    rates = await fetch_rates()
    subscription_ids = []
    async for subscription in subscriptions:
        is_time_passed = time_passed(
            subscription['last_sent'], subscription['interval'] * 60
        )
        user_data = users[subscription['user_id']]
        if is_time_passed and user_data['state'] == 'free':
            await process_subscription(subscription, user_data, rates, texts, bot)
            subscription_ids.append(subscription['_id'])
    await subscriptions_mgr.update_date_many(subscription_ids)
