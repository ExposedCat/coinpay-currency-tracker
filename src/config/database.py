from os import getenv

from aiogram import Dispatcher
from motor.motor_asyncio import AsyncIOMotorClient

from middlewares.database import DatabaseMiddleware

from services.db_users import UsersMgr
from services.db_subscriptions import SubscriptionsMgr


def init_db() -> tuple[UsersMgr, SubscriptionsMgr]:
    db_name = getenv('DB_NAME')

    db = AsyncIOMotorClient(
        'mongodb://{db_host}/{db_name}'.format(
            # TODO: Use authorized connection
            # db_user=getenv('DB_USER'),
            # db_password=getenv('DB_PASSWORD'),
            db_host=getenv('DB_HOST'),
            db_name=db_name,
        )
    )

    users_mgr = UsersMgr(db[db_name])
    subscriptions_mgr = SubscriptionsMgr(db[db_name])

    return users_mgr, subscriptions_mgr


def inject_database(
    users_mgr: UsersMgr, subscriptions_mgr: SubscriptionsMgr, dispatcher: Dispatcher
):
    dispatcher.setup_middleware(DatabaseMiddleware(users_mgr, subscriptions_mgr))
