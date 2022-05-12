import requests
from bs4 import BeautifulSoup

news_data = requests.get('https://www.sbbit.jp/index2.rss')
soup = BeautifulSoup(news_data.text, 'html.parser')

for news in soup.findAll('item'):
    print(news.title.text)
