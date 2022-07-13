import requests

url = 'https://httpbin.org/post'
params = {'somekey': 'somevalue'}
r = requests.post(url, data = params)
print(r.status_code)
print(r.url)
print(r.text)
