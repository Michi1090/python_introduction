from wsgiref.util import request_uri
import requests

base_url = 'https://zipcloud.ibsnet.co.jp/api/search'
query_parameter = '?zipcode='
zipcode = '6510077'
request_url = base_url + query_parameter + zipcode
print(request_url)
result = requests.get(request_url).json()
print(result)
