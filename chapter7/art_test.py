import requests

api_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
respose = requests.get(api_url)
respose_dict = respose.json()
total = respose_dict['total']

print(total)
