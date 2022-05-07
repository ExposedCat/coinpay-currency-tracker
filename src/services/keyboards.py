from data.type_aliases import TranslateFunc
from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def build_main_menu(
    translate: TranslateFunc,
    notifications_enabled: bool,
):
    toggle_button = (
        'button_disable_notifications'
        if notifications_enabled
        else 'button_enable_notifications'
    )
    keyboard = ReplyKeyboardMarkup(
        [
            [translate('button_subscriptions')],
            [translate(toggle_button)],
        ],
        resize_keyboard=True,
    )
    return keyboard


def build_currencies_keyboard(currencies: tuple[str]):
    keyboard = InlineKeyboardMarkup()
    buttons = []
    for name in currencies:
        button = InlineKeyboardButton(
            text=name,
            callback_data=f'buy_{name}',
        )
        buttons.append(button)
    keyboard.add(*buttons)
    return keyboard


def build_pairs_keyboard(currency: str, pairs: tuple[str]):
    keyboard = InlineKeyboardMarkup()
    buttons = []
    for name in pairs:
        button = InlineKeyboardButton(
            text=name,
            callback_data=f'pair_{currency}_{name}',
        )
        buttons.append(button)
    keyboard.add(*buttons)
    return keyboard
