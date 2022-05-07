from aiogram.dispatcher.handler import ctx_data
from aiogram.dispatcher.filters import Filter

from entities.user import User


class StateFilter(Filter):
    def __init__(self, state: str):
        self.state = state

    async def check(self, _):
        data = ctx_data.get()
        user: User = data.get('user')
        return user.get('state') == self.state
