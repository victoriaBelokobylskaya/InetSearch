import requests
from pprint import pprint
import json

access_token_vk='a7abdff511e41a98d81952d1e24b0c6a32ecfd97285746bf2518c870cb9a37622aa8604715a8029216f45'
user_id='709179'

vk_link = 'https://api.vk.com/method/groups.getMembers'

ver = '5.120'
group_id = 'upcharisma'
fields = 'sex,bdate,city'
filter = 'friends'

group_params = {'group_id': group_id,
                'v': ver,
                'fields': fields,
                'filter': filter,
                'access_token': access_token_vk}

response = requests.get(vk_link,params=group_params)
if response.ok:
    data = response.json()
    pprint(data)
    with open('response_vk.json', 'w') as f:
         f.write(json.dumps(data))