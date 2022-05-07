from os import getenv

from aiogram import Dispatcher
from motor.motor_asyncio import AsyncIOMotorClient

from middlewares.database import DatabaseMiddleware

from services.db_users import UsersMgr


def init_db() -> UsersMgr:
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

    return users_mgr


def inject_database(users_mgr: UsersMgr, dispatcher: Dispatcher):
    dispatcher.setup_middleware(DatabaseMiddleware(users_mgr))
