from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from pymongo import ReturnDocument

from datetime import datetime as date
from entities.user import User


class UsersMgr:
    def __init__(self, database: AsyncIOMotorDatabase):
        self._db: AsyncIOMotorCollection = database['users']

    async def get_or_create_user(self, user_id: int, lang: str = 'en') -> dict:
        document = {
            'id': user_id,
            'lang': lang,
            'date': date.now(),
            'subscriptions': [],
            'state': 'free',
            'notifications_enabled': True,
            'pair': None,
        }
        user = await self._db.find_one_and_update(
            {'id': user_id, 'lang': lang},
            {'$setOnInsert': document},
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )
        return User(self, user)

    def get_users(self):
        users = self._db.find()
        return users

    async def update_user(self, user_id: int, updates: dict):
        if updates is None:
            updates = {}
        await self._db.update_one(
            {'id': user_id},
            {'$set': updates},
        )

    async def find_and_update_user(self, user_id: int, updates: dict) -> dict:
        if updates is None:
            updates = {}
        user = await self._db.find_one_and_update(
            {'id': user_id},
            {'$set': updates},
            return_document=ReturnDocument.AFTER,
        )
        return user
