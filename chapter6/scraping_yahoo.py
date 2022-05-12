import requests
from bs4 import BeautifulSoup

html_data = requests.get('https://www.yahoo.co.jp/')
soup = BeautifulSoup(html_data.text, 'html.parser')
result = soup.title
print(result)
