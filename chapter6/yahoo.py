import requests
import pprint

r = requests.get('https://www.yahoo.co.jp')
pprint.pprint(r.text)
