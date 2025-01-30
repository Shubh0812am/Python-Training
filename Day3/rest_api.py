# consume rest APIs 

import requests

api_url = 'https://jsonplaceholder.typicode.com/users/1'

response =  requests.get(api_url)

data = response.json()

print(data['name'], data['email'])