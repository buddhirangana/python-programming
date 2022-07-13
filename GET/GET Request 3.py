import requests
r = requests.get('https://httpbin.org/obvious-incorrect')
print(r.status_code)
print(r.url)
print(r.text)
