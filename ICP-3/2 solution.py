import requests
from bs4 import BeautifulSoup
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(html.content, "html.parser")
print(soup.h1)
for link in soup.find_all('a'):
    print(link.get('href'))
