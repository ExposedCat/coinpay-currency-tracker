from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from pymongo import ReturnDocument

from datetime import datetime as date


class SubscriptionsMgr:
    def __init__(self, database: AsyncIOMotorDatabase):
        self._db: AsyncIOMotorCollection = database['subscriptions']

    async def update_or_create(self, currencies: str, interval: int, user_id: int):
        document = {
            'user_id': user_id,
            'currencies': currencies,
            'last_sent': date.now(),
            'interval': interval,
        }
        await self._db.find_one_and_update(
            {
                'user_id': user_id,
                'currencies': currencies,
            },
            {'$set': document},
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )

    def get_all(self):
        subscriptions = self._db.find()
        return subscriptions

    def get_by_user(self, user_id: int):
        subscriptions = self._db.find({'user_id': user_id})
        return subscriptions

    async def update_date_many(self, subscription_ids: list[int]):
        now = date.now()
        await self._db.update_one(
            {'_id': {'$in': subscription_ids}},
            {'$set': {'last_sent': now}},
        )

    async def delete(self, subscription_id: int):
        await self._db.delete_one({'_id': subscription_id})
