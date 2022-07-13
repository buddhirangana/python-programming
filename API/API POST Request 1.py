import requests

BASE_URL = 'https://vehicleapi.com'

vehicle_entity = {  "motorvehicles": {      "vehicle": {"type": "car", "registration_no": "CBB1456",      "make": "Toyota",      "model": "Premio"    },    "owner": {      "first_name": "Amal",      "last_name": "Perera", "nic": "900324770V" }  }}
response = requests.post(f"{BASE_URL}/vehicles", json=vehicle_entity)
print(response.status_code)
print(response.json())
