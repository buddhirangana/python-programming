import requests

BASE_URL = 'https://vehicleapi.com'

response = requests.delete(f"{BASE_URL}/vehicles/CBB1456")
print(response.status_code)
print(response.json())
