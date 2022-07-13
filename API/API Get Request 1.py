import requests

BASE_URL = 'https://vehicleapi.com'

response = requests.get(f"{BASE_URL}/vehicles")

print(response.status_code)
print(response.json())
