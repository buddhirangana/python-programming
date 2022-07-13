import requests

BASE_URL = 'https://vehicleapi.com'

updated_entity = {"owner": {"first_name": "Marlon",      "last_name": "Samuels", "nic": “870124770V" }  }
response = requests.patch(f"{BASE_URL}/vehicles/CBB1456", json=updated_entity)
print(response.status_code)
print(response.json())
