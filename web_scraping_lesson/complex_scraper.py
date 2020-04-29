import itertools
import json
import random
from hashlib import md5
from os import listdir
from os.path import dirname, join

from bs4 import BeautifulSoup
from stringcase import snakecase


def encode_dealer_name(name: str) -> str:
    return (md5(
        snakecase(name)
            .lower()
            .encode())
            .hexdigest())


def encode_vin(vin: str) -> str:
    encoded_vin = ""
    characters = list(itertools.chain(range(48, 58), range(65, 91)))

    for _, i in enumerate(vin):
        encoded_vin += chr(random.choice(characters))

    return encoded_vin


html_file_dir = join(dirname(__file__), "html_files")
html_files = [join(html_file_dir, f) for f in listdir(html_file_dir)]

complete_vehicle_listings = []

for html_file in html_files:
    with open(html_file, "r") as reader:
        html = reader.read()

    soup = BeautifulSoup(html, "html.parser")
    scripts = [s for s in soup.select('[type="application/ld+json"]') if not s.attrs.get("id")]
    vehicle_listings = json.loads(scripts[0].string)

    for vehicle_listing in vehicle_listings:
        complete_vehicle_listings.append(vehicle_listing)

vehicles = {i["vehicleIdentificationNumber"]: {
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
} for i in complete_vehicle_listings if i["offers"]["seller"].get("aggregateRating") is not None}

inventory = dict()

for i in complete_vehicle_listings:
    if i["offers"]["seller"].get("aggregateRating") is None:
        continue

    key = encode_dealer_name(i["offers"]["seller"]["name"])

    if not inventory.get(key):
        inventory[key] = {
            "seller": {},
            "offers": []
        }

    inventory[key]["offers"].append({
        "vin": encode_vin(i["vehicleIdentificationNumber"]),
        "make": i["brand"]["name"],
        "model": i["name"],
        "price": i["offers"]["price"],
        "currency": i["offers"]["priceCurrency"],
        "color": i["color"].lower()
    })

    inventory[key]["seller"] = {
        "rating": i["offers"]["seller"]["aggregateRating"]["ratingValue"],
        "reviews": i["offers"]["seller"]["aggregateRating"]["reviewCount"]
    }

    inventory[key]["offerCount"] = len(inventory[key]["offers"])

with open("inventory.json", "w", encoding="utf8") as writer:
    writer.write(json.dumps(inventory))

final_inventory = []

for i in inventory:
    seller = {
        "name": i,
        "vehicleCount": inventory[i]["offerCount"],
        **inventory[i]["seller"],
        "offers": [inventory[i]["offers"]]
    }
    final_inventory.append(seller)

with open("final_inventory.json", "w", encoding="utf8") as writer:
    writer.write(json.dumps(final_inventory))
