import logging

from config.bot import init_bot, start_bot
from config.database import init_db

logging.basicConfig(level=logging.INFO)

database = init_db()
dispatcher = init_bot(database)
start_bot(dispatcher)
