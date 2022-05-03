from typing import Callable


def build_get_text_func(texts: dict, lang: str) -> Callable[[str, dict], str]:
    def get_text(template_id: str, data: dict = None) -> str:
        if not data:
            data = {}
        if not lang in texts or not template_id in texts[lang]:
            return template_id
        return texts[lang][template_id].format(**data)
    return get_text
