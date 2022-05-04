from os import getenv
from typing import Tuple

from aiogram import Bot, Dispatcher, executor, types

from filters.button_click_filter import ButtonClickFilter

from config.localization import setup_locale_engine
from handlers.start import handler as _cmd_start
from handlers.subscriptions_list import handler as _cmd_subs_list


def _setup_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(commands=['start'], callback=_cmd_start)
    dispatcher.register_message_handler(
        _cmd_subs_list, ButtonClickFilter('button_subscriptions')
    )


def init_bot() -> Tuple[Bot, Dispatcher]:
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
