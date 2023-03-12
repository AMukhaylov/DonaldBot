import requests
from bs4 import BeautifulSoup as BS
import lxml

url = 'https://pokur.su/rub/kgs/1/'
r = requests.get(url)
soup = BS(r.text, 'lxml')
curs = soup.find("div", {"class": "blockquote-classic"}).text

print(curs)