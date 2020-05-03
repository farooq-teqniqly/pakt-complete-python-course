from enum import Enum
from typing import Dict
from babel.numbers import format_currency
from cachetools import cached, TTLCache

import logging
import requests
import time

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
        self._locale = "en_US"

    @cached(cache=TTLCache(maxsize=1024, ttl=3600))
    def _get_latest_rates(self) -> Dict[str, float]:
        response = requests.get(
            OpenExchangeClient.ENDPOINT_FORMAT.format("latest", self._api_key)
        )

        return response.json()["rates"]

    def convert(self, convert_to: Currency, amount: float) -> str:
        start = time.time()
        convert_to_amount = amount * self._get_latest_rates()[convert_to.value]
        end = time.time()

        logger.debug(f"Convert ran in {end - start} seconds.")

        return (
            f"{format_currency(amount, 'USD', locale=self._locale)} "
            f"= {format_currency(convert_to_amount, convert_to.value, locale=self._locale, decimal_quantization=False)}"
        )
