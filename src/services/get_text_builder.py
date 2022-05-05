import json
from data.type_aliases import TranslateFunc


def build_get_text_func(texts: dict, lang: str) -> TranslateFunc:
    def get_text(template_id: str, data: dict = None) -> str:
        if not data:
            data = {}
        if not lang in texts or not template_id in texts[lang]:
            return template_id
        return texts[lang][template_id].format(**data)

    return get_text


def get_texts(texts_path: str) -> dict:
    if not texts_path:
        texts_path = 'src/data/texts.json'
    with open(texts_path) as file:
        data = json.load(file)
    return data
