import json

with open("data.json", "r") as file:
    info = json.load(file)

print(info["name"])
print(info["age"])
print(info["city"])