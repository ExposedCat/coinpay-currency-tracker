from data.type_aliases import TranslateFunc
from aiogram.types import Message


async def handler(message: Message, translate: TranslateFunc):
    # TODO: Get real user subsriptions
    subscriptions = (
        {'buy': 'BTC', 'sell': 'USDT', 'interval': 5},
        {'buy': 'ETH', 'sell': 'USDT', 'interval': 10},
        {'buy': 'XRP', 'sell': 'UAH', 'interval': 5},
    )
    subscriptions_string = '\n'.join(
        [translate('component_subscription', data) for data in subscriptions]
    )
    response_string = translate('subscriptions', {'list': subscriptions_string})
    # TODO: Send each subscription as separate message
    await message.answer(
        response_string,
        # TODO: Add button to add subscription
    )
