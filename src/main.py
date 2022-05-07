import logging

from config.bot import init_bot, start_bot
from config.database import init_db

logging.basicConfig(level=logging.INFO)



start_bot(dispatcher)
users_mgr = init_db()
dispatcher = init_bot(users_mgr)
