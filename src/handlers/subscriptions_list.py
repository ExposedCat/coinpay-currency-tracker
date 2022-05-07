from data.type_aliases import TranslateFunc
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton as Button,
)

from entities.user import User


async def handler(message: Message, translate: TranslateFunc, user: User):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        translate('button_add_notification'),
        translate('button_main_menu'),
    ]
    keyboard.add(*buttons)
    data = {
        'is_empty': ''
        if len(user.get('subscriptions'))
        else translate('component_empty')
    }
    await message.answer(
        translate('subscriptions', data),
        reply_markup=keyboard,
    )
    for subscription in user.get('subscriptions'):
        keyboard = InlineKeyboardMarkup()
        button = Button(
            text=translate('button_remove_notification'),
            callback_data=f'remove_notification_{id}',
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
