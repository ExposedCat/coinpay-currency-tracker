from aiogram import Bot
from aiogram.utils.exceptions import Throttled
from services.db_users import UsersMgr

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
    return delta.seconds >= seconds


async def process_subscription(
    subscription: dict, user: dict, rates: dict, texts: dict, bot: Bot
):
    if time_passed(subscription['last_sent'], subscription['interval']):
        print('time passed')
        pair = subscription['currencies']
        rate = rates[pair] if pair in rates else 0
        await _send_notification(
            bot,
            user_id=user['id'],
            lang=user['lang'],
            pair=pair,
            rate=rate,
            texts=texts,
        )
    else:
        print('time NOT passed')


async def send_notifications(users_mgr: UsersMgr, texts: dict):
    bot = Bot.get_current()
    users = users_mgr.get_users()
    rates = await fetch_rates()
    async for user in users:
        for subscription in user['subscriptions']:
            await process_subscription(subscription, user, rates, texts, bot)
