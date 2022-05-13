import requests, pprint

search_api_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?'
query_parameter = 'q=python&hasImage=true'
search_url = search_api_url + query_parameter
print(search_url)

search_response = requests.get(search_url)
pprint.pprint(search_response.json())

# -------------------------------------------------------------------------------------------------
get_object_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/435864'
object_response = requests.get(get_object_url)

result_url = object_response.json()['objectURL']
print(result_url)

result_title = object_response.json()['title']
print(result_title)

result_img = object_response.json()['primaryImageSmall']
print(result_img)
