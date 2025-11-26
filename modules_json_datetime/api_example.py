import requests

r = requests.get("https://api.github.com")
print("Status Code:", r.status_code)

try:
    print("Data:", r.json())
except ValueError:
    print("No JSON data received.")