import json


def load_json(path: str) -> dict:
    with open(path) as file:
        data = json.load(file)
    return data
