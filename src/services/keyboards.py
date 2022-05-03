from data.type_aliases import TranslateFunc
from aiogram import types


def build_main_menu(
    translate: TranslateFunc,
    notifications_enabled: bool,
):
    toggle_button = (
        'button_disable_notifications'
        if notifications_enabled
        else 'button_enable_notifications'
    )
    keyboard = types.ReplyKeyboardMarkup(
        [
            [translate('button_subscriptions')],
            [translate(toggle_button)],
        ],
        resize_keyboard=True,
    )
    return keyboard
