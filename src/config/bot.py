from os import getenv

from typing import Callable
from aiogram import Bot, Dispatcher, executor, types
from services.db_users import UsersMgr


from filters.button_click_filter import ButtonClickFilter
from filters.inline_click_filter import InlineClickFilter

from config.localization import inject_locale_engine
from config.database import inject_database

from handlers.start import handler as _cmd_start
from handlers.main_menu import handler as _cmd_main_menu
from handlers.subscriptions_list import handler as _cmd_subs_list
from handlers.toggle_notifications import (
    handler_on as _cmd_notify,
    handler_off as _cmd_not_notify,
)
from handlers.unkown import handler as _unknown_command
from handlers.add_notification import handler as _cmd_add_notification
from handlers.choose_currency_buy import handler as _click_currency_buy
from handlers.choose_pair import handler as _click_pair


def setup_handlers(dispatcher: Dispatcher):
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
    dispatcher.register_message_handler(
        _cmd_add_notification, ButtonClickFilter('button_add_notification')
    )
    dispatcher.register_callback_query_handler(
        _click_currency_buy, InlineClickFilter('buy_')
    )
    dispatcher.register_callback_query_handler(
        _click_pair, InlineClickFilter('pair_')
    )
    dispatcher.register_message_handler(_unknown_command)


def init_bot(users_mgr: UsersMgr) -> Dispatcher:
    bot = Bot(
        token=getenv('BOT_TOKEN'),
        parse_mode=types.ParseMode.HTML,
    )
    dispatcher = Dispatcher(bot)
    inject_database(users_mgr, dispatcher)
    inject_locale_engine(dispatcher)
    setup_handlers(dispatcher)
    return dispatcher


def start_bot(dispatcher: Dispatcher, on_start: Callable, on_end: Callable):
    executor.start_polling(
        dispatcher,
        on_startup=on_start,
        on_shutdown=on_end,
    )
