from typing import Callable, TypeAlias


TranslateFunc: TypeAlias = Callable[[str, dict], str]


class PairNotFound(Exception):
    pass
