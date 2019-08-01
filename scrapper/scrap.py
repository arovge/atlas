import requests
from bs4 import BeautifulSoup

url = 'https://google.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)