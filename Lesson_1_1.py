import requests
from pprint import pprint
import json

user = 'victoriaBelokobylskaya'

target_link = f'https://api.github.com/users/{user}/repos'
response = requests.get(target_link)
repos = []
if response.ok:
    data = response.json()
    with open('response.json', 'w') as f:
         f.write(json.dumps(data))

    for data_list in data:
        for key, value in data_list.items():
            if key == 'full_name':
                repos.append(value)

print(f'Репозитории пользователя: {repos}')
