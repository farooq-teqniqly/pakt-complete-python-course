from os import getenv
import requests
from babel.numbers import format_currency
from dotenv import load_dotenv

settings = load_dotenv(".env")
api_key = getenv("API_KEY")

ENDPOINT_FORMAT = (
    "https://openexchangerates.org/api/{0}.json?app_id={1}&prettyprint=false"
)

response = requests.get(ENDPOINT_FORMAT.format("latest", api_key))
rates = response.json()["rates"]

us_amt: float = 1.00
uk_amt: float = us_amt * rates["JPY"]


print(
    f"{format_currency(us_amt, 'USD', locale='en_US')} "
    f"= {format_currency(uk_amt, 'JPY', locale='en_US', decimal_quantization=False)}"
)
