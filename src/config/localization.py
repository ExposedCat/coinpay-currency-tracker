import json
from typing import Callable

from aiogram import Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware


def _build_get_text_func(texts: dict, lang: str) -> Callable[[str, dict], str]:
    def get_text(template_id: str, data: dict = None) -> str:
        if not data:
            data = {}
        if not lang in texts or not template_id in texts[lang]:
            return template_id
        return texts[lang][template_id].format(**data)
    return get_text


class I18nMiddleware(BaseMiddleware):
    def __init__(self, texts_path: str = 'src/data/texts.json'):
        super().__init__()
        with open(texts_path) as texts_file:
            self._texts = json.load(texts_file)

    async def on_process_message(self, message: types.Message, data: dict) -> None:
        lang = message.from_user.language_code or 'en'
        data['text'] = _build_get_text_func(self._texts, lang)


def setup_locale_engine(dispatcher: Dispatcher) -> None:
    dispatcher.setup_middleware(I18nMiddleware())
