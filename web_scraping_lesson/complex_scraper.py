import json
from hashlib import md5
from pprint import pprint as pp

from bs4 import BeautifulSoup
from stringcase import snakecase


def encode_dealer_name(name: str) -> str:
    return (md5(
        snakecase(name)
            .lower()
            .encode())
            .hexdigest())


with open("complex.html", "r") as reader:
    html = reader.read()

soup = BeautifulSoup(html, "html.parser")
scripts = [s for s in soup.select('[type="application/ld+json"]') if not s.attrs.get("id")]
vehicle_listings = json.loads(scripts[0].string)

with open("vehicle_listings.json", "w", encoding="utf8") as writer:
    writer.write(str(vehicle_listings))

summary = {i["vehicleIdentificationNumber"]: {
    "offer": {
        "make": i["brand"]["name"],
        "model": i["name"],
        "price": i["offers"]["price"],
        "currency": i["offers"]["priceCurrency"],
        "color": i["color"].lower()
    },
    "seller": {
        "name": encode_dealer_name(i["offers"]["seller"]["name"]),
        "rating": i["offers"]["seller"]["aggregateRating"]["ratingValue"],
        "reviews": i["offers"]["seller"]["aggregateRating"]["reviewCount"]
    }
} for i in vehicle_listings if i["offers"]["seller"].get("aggregateRating") is not None}

pp(summary)
print(len(summary))
