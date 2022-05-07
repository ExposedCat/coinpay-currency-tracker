from aiogram import Bot
from aiogram.utils.exceptions import Throttled
from services.db_users import UsersMgr

from services.get_text_builder import build_get_text_func, get_texts
from services.api import fetch_rates


async def _send_notification(
    bot: Bot,
    user_id: int,
    texts: dict,
    lang: str,
    pair: str,
    rate: float,
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


async def send_notifications(users_mgr: UsersMgr):
    texts = get_texts()
    bot = Bot.get_current()
    users = users_mgr.get_users()
    rates = await fetch_rates()
    async for user in users:
        for subscription in user['subscriptions']:
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
