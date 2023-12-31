import json
import requests as r
from config import all_values

class APIException(Exception):
    pass

class StaticValue:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote not in all_values and base not in all_values and not amount.isdigit():
            raise APIException(f'Кодов валюты {base} и {quote} не существует, а также {amount} не является числом!')
        elif quote not in all_values and base not in all_values:
            raise APIException(f'Кодов валюты {base} и {quote} не существует')
        elif base not in all_values:
            raise APIException(f'Кода валюты {base} не существует')
        elif quote not in all_values:
            raise APIException(f'Кода валюты {quote} не существует')
        elif not amount.isdigit():
            raise APIException(f'{amount} не является числом!')
        text = r.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        result = json.loads(text.content)
        return result