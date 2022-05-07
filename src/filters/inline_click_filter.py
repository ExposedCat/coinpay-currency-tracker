from aiogram.types import CallbackQuery

from aiogram.dispatcher.filters import Filter


class InlineClickFilter(Filter):
    def __init__(self, button_id: str):
        self.button_id = button_id

    async def check(self, call: CallbackQuery):
        return call.data.startswith(self.button_id)
