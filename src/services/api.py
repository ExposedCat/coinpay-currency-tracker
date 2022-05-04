import os
from data.type_aliases import PairNotFound
from services.send_request import send_request


api = lambda path: f'{os.environ["API_ENDPOINT"]}/{path}'


async def get_currencies() -> set[str]:
    response = await send_request(api('pair'))
    currencies = set([pair['currency_to_spend'] for pair in response['pairs']])
    return currencies


async def get_pair(currency: str) -> list[str]:
    response = await send_request(api('pair'))
    currencies = [
        pair['currency_to_get']
        for pair in response['pairs']
        if pair['currency_to_spend'] == currency
    ]
    return currencies


async def get_rate(sale_currency: str, buy_currency: str) -> float:
    response = await send_request(api('exchange_rate'))
    try:
        rate = next(
            pair['price']
            for pair in response['rates']
            if pair['pair'] == f'{sale_currency}_{buy_currency}'
        )
    except StopIteration:
        raise PairNotFound
    return rate
