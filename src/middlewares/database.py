from aiogram.dispatcher.middlewares import BaseMiddleware

from motor.motor_asyncio import AsyncIOMotorDatabase


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, database: AsyncIOMotorDatabase):
        super().__init__()
        self._database = database

    async def on_pre_process_message(self, _, data: dict):
        data['db'] = self._database

    on_pre_process_callback_query = on_pre_process_message
