import time
from os import getenv
from call_api_lesson.open_exchange_client import OpenExchangeClient, Currency
from dotenv import load_dotenv
import logging

logger = logging.getLogger("open_exchange_client_app")
log_entry_format = (
    "%(asctime)s %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s"
)
logging.basicConfig(level=logging.DEBUG, format=log_entry_format)
logging.Formatter.converter = time.gmtime

settings = load_dotenv(".env")
api_key = getenv("API_KEY")

client = OpenExchangeClient(api_key)

try:
    while True:
        convert_to_str = input("Enter the currency to convert to: ")
        amount_str = input("Enter the amount: ")

        convert_to = Currency[convert_to_str]
        amount = float(amount_str)

        print(client.convert(convert_to, amount))
except KeyboardInterrupt:
    print("Bye.")
