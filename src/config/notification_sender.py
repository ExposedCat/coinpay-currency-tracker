from services.db_users import UsersMgr
from services.db_subscriptions import SubscriptionsMgr

import asyncio
from services.notifications_sender import send_notifications
from services.get_text_builder import get_texts


async def job(users_mgr: UsersMgr, subscriptions_mgr: SubscriptionsMgr, texts: dict):
    while True:
        await send_notifications(users_mgr, subscriptions_mgr, texts)
        await asyncio.sleep(60)


def run_notification_sender(
    users_mgr: UsersMgr, subscriptions_mgr: SubscriptionsMgr
):
    loop = asyncio.get_event_loop()
    texts = get_texts()
    return loop.create_task(job(users_mgr, subscriptions_mgr, texts))
