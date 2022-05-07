from services.db_users import UsersMgr

import asyncio
from services.notifications_sender import send_notifications
from services.get_text_builder import get_texts


async def job(users_mgr: UsersMgr, texts: dict):
    while True:
        await send_notifications(users_mgr, texts)
        await asyncio.sleep(60)


def run_notification_sender(users_mgr: UsersMgr):
    loop = asyncio.get_event_loop()
    texts = get_texts()
    return loop.create_task(job(users_mgr, texts))
