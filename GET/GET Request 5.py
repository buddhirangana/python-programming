import requests
payload = {'q': 'sri+lanka'}
r = requests.get('https://www.google.com/search?', params=payload)
print(r.url)
print (r.text)
