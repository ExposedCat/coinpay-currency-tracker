import logging

import asyncio

from config.bot import init_bot, start_bot
from config.database import init_db
from config.notification_sender import run_notification_sender

asyncio.set_event_loop(asyncio.new_event_loop())
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def on_start(_):
    log.info('Running notification sender')
    run_notification_sender(users_mgr, subscriptions_mgr)


async def on_end(_):
    pass


users_mgr, subscriptions_mgr = init_db()
dispatcher = init_bot(users_mgr, subscriptions_mgr)
start_bot(dispatcher, on_start, on_end)
