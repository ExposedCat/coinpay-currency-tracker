from os import getenv

from aiogram import Dispatcher

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from middlewares.database import DatabaseMiddleware


def init_db() -> AsyncIOMotorDatabase:
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

    return db[db_name]


def inject_database(database: AsyncIOMotorDatabase, dispatcher: Dispatcher):
    dispatcher.setup_middleware(DatabaseMiddleware(database))
