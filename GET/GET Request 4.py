import requests
r = requests.get('https://www.google.com/search?q=Python')
print(r.status_code)
print(r.url)
print(r.text)
