from os import getenv

from aiogram import Bot, Dispatcher, executor, types

from handlers.start import handler as start_handler


def _setup_handlers(bot: Bot, dispatcher: Dispatcher):
    @dispatcher.message_handler(commands=['start'])
    async def handle_start(message: types.Message):
        await start_handler(message)


def init_bot():
    bot = Bot(token=getenv('BOT_TOKEN'))
    dispatcher = Dispatcher(bot)
    _setup_handlers(bot, dispatcher)
    return bot, dispatcher


def start_bot(dispatcher: Dispatcher):
    executor.start_polling(dispatcher)
