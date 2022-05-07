from services.db_users import UsersMgr

import asyncio
from services.notifications_sender import send_notifications


async def job(users_mgr: UsersMgr):
    while True:
        await send_notifications(users_mgr)
        await asyncio.sleep(5)


def run_notification_sender(users_mgr: UsersMgr):
    loop = asyncio.get_event_loop()
    return loop.create_task(job(users_mgr))
