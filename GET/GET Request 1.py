import requests
r = requests.get('https://uom.lk')
print(r.status_code)
print(r.url)
print(r.text)
