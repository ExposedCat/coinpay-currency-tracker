from aiogram import Dispatcher
from middlewares.i18n import I18nMiddleware


def setup_locale_engine(dispatcher: Dispatcher) -> None:
    dispatcher.setup_middleware(I18nMiddleware())
