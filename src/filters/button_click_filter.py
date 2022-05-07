from aiogram.types import Message

from aiogram.dispatcher.handler import ctx_data
from aiogram.dispatcher.filters import Filter


class ButtonClickFilter(Filter):
    def __init__(self, button_id: str):
        self.button_id = button_id

    async def check(self, message: Message):
        data = ctx_data.get()
        translate = data.get('translate')
        return message.text == translate(self.button_id)
