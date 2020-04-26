import json

with open("vehicle_makes.json", "r") as reader:
    json_content = json.load(reader)

print(f"There are {json_content['Count']} makes.")

selected_makes = []

for _, make in enumerate(json_content['Results']):
    if make['Make_Name'] in ["Ford", "Mercedes-Benz", "BMW"]:
        selected_makes.append(make)

print(json.dumps(selected_makes))


