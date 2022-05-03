from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware

from services.load_json import load_json as _load_json
from services.get_text_builder import (
    build_get_text_func as _build_get_text_func,
)


class I18nMiddleware(BaseMiddleware):
    def __init__(self, texts_path: str = 'src/data/texts.json'):
        super().__init__()
        self._texts = _load_json(texts_path)

    async def on_process_message(self, message: Message, data: dict):
        lang = message.from_user.language_code or 'en'
        data['translate'] = _build_get_text_func(self._texts, lang)
