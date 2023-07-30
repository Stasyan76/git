import json
import requests as r
from config import all_values

class APIException(Exception):
    pass

class StaticValue:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if base not in all_values:
            raise APIException(f'Кода валюты {base} не существует')
        elif quote not in all_values:
            raise APIException(f'Кода валюты {quote} не существует')
        elif not amount.isdigit():
            raise APIException(f'{amount} не является числом!')

        text = r.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        result = json.loads(text.content)

        return result