import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Python'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the h3 tags
headings = soup('h3')
for heading in headings:
    print(heading.find('div').text)
    #print(heading.parent)
    print(heading.parent.get('href'))
