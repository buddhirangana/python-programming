import requests
r = requests.get('https://httpbin.org/get')
print(r.status_code)
print(r.url)
print(r.text)
