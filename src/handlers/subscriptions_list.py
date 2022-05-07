from data.type_aliases import TranslateFunc
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton as Button,
)


async def handler(
    message: Message, translate: TranslateFunc, subscriptions: list[dict]
):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        translate('button_add_notification'),
        translate('button_main_menu'),
    ]
    keyboard.add(*buttons)
    await message.answer(
        translate('subscriptions'),
        reply_markup=keyboard,
    )
    sent = False
    async for subscription in subscriptions:
        keyboard = InlineKeyboardMarkup()
        button = Button(
            text=translate('button_remove_notification'),
            callback_data=f'remove_notification_{subscription["_id"]}',
        )
        keyboard.add(button)
        buy, sell = subscription['currencies'].split('_')
        subscription_data = {
            'buy': buy,
            'sell': sell,
            'interval': subscription['interval'],
        }
        await message.answer(
            translate('component_subscription', subscription_data),
            reply_markup=keyboard,
        )
        sent = True
    if not sent:
        await message.answer(translate('component_empty'))
