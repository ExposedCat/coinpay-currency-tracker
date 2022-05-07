from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware

from services.db_users import UsersMgr
from services.db_subscriptions import SubscriptionsMgr


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, users_mgr: UsersMgr, subscriptions_mgr: SubscriptionsMgr):
        super().__init__()
        self._users_mgr = users_mgr
        self._subscriptions_mgr = subscriptions_mgr

    async def on_pre_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        user_lang = message.from_user.language_code or 'en'
        data['user'] = await self._users_mgr.get_or_create_user(user_id, user_lang)
        data['subscriptions'] = self._subscriptions_mgr.get_by_user(user_id)
        data['subscriptions_mgr'] = self._subscriptions_mgr

    on_pre_process_callback_query = on_pre_process_message
