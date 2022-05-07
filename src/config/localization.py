from aiogram import Dispatcher
from middlewares.i18n import I18nMiddleware


def inject_locale_engine(dispatcher: Dispatcher):
    dispatcher.setup_middleware(I18nMiddleware())
