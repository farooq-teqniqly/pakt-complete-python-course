from enum import Enum
from typing import Dict
from babel.numbers import format_currency

import logging
import requests

logger = logging.getLogger("open_exchange_client")


class Currency(Enum):
    USD = "USD"
    CAD = "CAD"
    JPY = "JPY"
    EUR = "EUR"
    GBP = "GBP"
    ISK = "ISK"
    MXP = "MXP"
    PKR = "PKR"


class OpenExchangeClient:

    ENDPOINT_FORMAT = (
        "https://openexchangerates.org/api/{0}.json?app_id={1}&prettyprint=false"
    )

    def __init__(self, api_key: str):
        self._api_key = api_key
        self._cache: Dict[str, float] = None
        self._locale = "en_US"

    def convert(self, convert_to: Currency, amount: float):
        if not self._cache:
            logger.debug("Cache miss.")
            response = requests.get(
                OpenExchangeClient.ENDPOINT_FORMAT.format("latest", self._api_key)
            )
            self._cache = response.json()["rates"]

        convert_to_amount = amount * self._cache[convert_to.value]

        return (
            f"{format_currency(amount, 'USD', locale=self._locale)} "
            f"= {format_currency(convert_to_amount, convert_to.value, locale=self._locale, decimal_quantization=False)}"
        )
