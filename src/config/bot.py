from os import getenv

from aiogram import Bot, Dispatcher, executor, types

from filters.button_click_filter import ButtonClickFilter

from config.localization import setup_locale_engine

from handlers.start import handler as _cmd_start
from handlers.main_menu import handler as _cmd_main_menu
from handlers.subscriptions_list import handler as _cmd_subs_list
from handlers.toggle_notifications import (
    handler_on as _cmd_notify,
    handler_off as _cmd_not_notify,
)


def _setup_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(commands='start', callback=_cmd_start)
    dispatcher.register_message_handler(
        _cmd_subs_list, ButtonClickFilter('button_subscriptions')
    )
    dispatcher.register_message_handler(
        _cmd_main_menu, ButtonClickFilter('button_main_menu')
    )
    dispatcher.register_message_handler(
        _cmd_notify, ButtonClickFilter('button_enable_notifications')
    )
    dispatcher.register_message_handler(
        _cmd_not_notify, ButtonClickFilter('button_disable_notifications')
    )


def init_bot() -> tuple[Bot, Dispatcher]:
    bot = Bot(
        token=getenv('BOT_TOKEN'),
        parse_mode=types.ParseMode.HTML,
    )
    dispatcher = Dispatcher(bot)
    setup_locale_engine(dispatcher)
    _setup_handlers(dispatcher)
    return bot, dispatcher


def start_bot(dispatcher: Dispatcher):
    executor.start_polling(dispatcher)
