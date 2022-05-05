from aiogram import Bot

from datetime import datetime

from aiogram.utils.exceptions import Throttled
from services.get_text_builder import build_get_text_func, get_texts


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
        await bot.send_message(
            user_id,
            translate(
                'notification',
                {
                    'buy': buy,
                    'sell': sell,
                    'rate': rate,
                },
            ),
        )
    except Throttled:
        pass


async def send_notifications(rates: dict):
    texts = get_texts()
    bot = Bot.get_current()
    # TODO: Get real users
    users = (
        {
            'user_id': 849670500,
            'lang': 'en',
            'subscriptions': (
                {
                    'currencies': 'USDT_UAH',
                    'interval': 2,
                    'date': datetime(2020, 1, 1),
                },
            ),
        },
    )
    for user in users:
        for subscription in user['subscriptions']:
            pair = subscription['currencies']
            rate = rates[pair] if pair in rates else 0
            await _send_notification(
                bot,
                user_id=user['user_id'],
                lang=user['lang'],
                pair=pair,
                rate=rate,
                texts=texts,
            )
