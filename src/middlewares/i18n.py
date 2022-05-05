from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware

from services.get_text_builder import build_get_text_func, get_texts


class I18nMiddleware(BaseMiddleware):
    def __init__(self, texts_path: str = None):
        super().__init__()
        self._texts = get_texts(texts_path)

    async def on_pre_process_message(self, message: Message, data: dict):
        lang = message.from_user.language_code or 'en'
        data['translate'] = build_get_text_func(self._texts, lang)

    on_pre_process_callback_query = on_pre_process_message
