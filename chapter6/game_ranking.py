import requests
from bs4 import BeautifulSoup

game_ranking_html = requests.get('https://www.kamatari.org/blog/2021/best-games-of-2021/')
soup = BeautifulSoup(game_ranking_html.text, 'html.parser')
for game in soup.findAll('h2'):
    print(game.text)
