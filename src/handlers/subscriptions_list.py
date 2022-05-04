from data.type_aliases import TranslateFunc
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton as Button,
)


async def handler(message: Message, translate: TranslateFunc):
    # TODO: Get real user subsriptions
    subscriptions = (
        {'buy': 'BTC', 'sell': 'USDT', 'interval': 5, 'id': '0'},
        {'buy': 'ETH', 'sell': 'USDT', 'interval': 10, 'id': '1'},
        {'buy': 'XRP', 'sell': 'UAH', 'interval': 5, 'id': '2'},
    )
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        translate('button_add_notification'),
        translate('button_main_menu'),
    ]
    keyboard.add(*buttons)
    data = {
        'is_empty': '' if len(subscriptions) else translate('component_empty')
    }
    await message.answer(
        translate('subscriptions', data),
        reply_markup=keyboard,
    )
    for subscription in subscriptions:
        keyboard = InlineKeyboardMarkup()
        button = Button(
            text=translate('button_remove_notification'),
            callback_data=f'remove_notification_{id}',
        )
        keyboard.add(button)
        await message.answer(
            translate('component_subscription', subscription),
            reply_markup=keyboard,
        )
