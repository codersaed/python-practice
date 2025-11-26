import json

data = {
    "name": "Rahim",
    "age": 15,
    "city": "Dhaka"
}

# JSON file e save
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Saved!")