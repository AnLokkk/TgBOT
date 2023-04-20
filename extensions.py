import requests
import json
from config import coin

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def  convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException('Введена одна и таже валюта! \n Пример написания запроса: USD BTC 100')
        try:
            quote_ticker = coin[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = coin[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(
                f'не удалось обработать количество {amount} \n \n Формат написания запроса: USD BTC 100')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={coin[quote_ticker]}&tsyms={coin[base_ticker]}')
        total = json.loads(r.content)[coin[base]]

        return total