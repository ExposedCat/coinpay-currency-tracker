from os import getenv
from typing import Tuple

from aiogram import Bot, Dispatcher, executor, types

from config.localization import setup_locale_engine as _setup_locale_engine
from handlers.start import handler as start_handler


def _setup_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(
        commands=['start'], callback=start_handler
    )


def init_bot() -> Tuple[Bot, Dispatcher]:
    bot = Bot(token=getenv('BOT_TOKEN'), parse_mode=types.ParseMode.HTML)
    dispatcher = Dispatcher(bot)
    _setup_locale_engine(dispatcher)
    _setup_handlers(dispatcher)
    return bot, dispatcher


def start_bot(dispatcher: Dispatcher) -> None:
    executor.start_polling(dispatcher)
