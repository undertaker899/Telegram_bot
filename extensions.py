import requests
import json
from config import currency


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise APIException(f"Can't process currency {quote}")

        try:
            base_ticker = currency[base]
        except KeyError:
            raise APIException(f"Can't process currency {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Can't process amount of currency {amount}")

        if quote == base:
            raise APIException(f"Can't convert same currency {base}.")

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}'
        )
        sample = json.loads(r.content)[currency[base]] * amount

        return sample
