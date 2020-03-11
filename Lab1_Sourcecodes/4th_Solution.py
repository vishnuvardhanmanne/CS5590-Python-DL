import requests
from bs4 import BeautifulSoup
url = 'https://catalog.umkc.edu/course-offerings/graduate/comp-sci/'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
# Finding all the divs with class courseblock
res = soup.find_all('div', {'class': 'courseblock'})
# printing all the course names and course descriptions
for a in res:
  res1 = a.find('span', {'class': 'code'}).text
  res2 = a.find('p', {'class': 'courseblockdesc'}).text
  print(res1)
  print(res2)