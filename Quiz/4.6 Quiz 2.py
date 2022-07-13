import json

myVar = '{"name": "Bob", "languages": ["English", "French"]}'

myVar_dict = json.loads(myVar)
length = len(myVar_dict)
print(length)
