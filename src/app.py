import logging
from config.bot import init_bot, start_bot

logging.basicConfig(level=logging.INFO)

bot, dispatcher = init_bot()
start_bot(dispatcher)
