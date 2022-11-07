from config import MY_TOKEN, MY_USER, MY_GRAPHID
import requests
from datetime import datetime

#CONST
pixela_endpoint = 'https://pixe.la/v1/users'

headers = {
    'X-USER-TOKEN': MY_TOKEN
}

#CREATE YOUR USER ACCOUNT
user_params = {
    'token':MY_TOKEN,
    'username':MY_USER,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#CREATE A GRAPH DEFINITION
graph_endpoint = f'{pixela_endpoint}/{MY_USER}/graphs'

graph_config = {
    'id': MY_GRAPHID,
    'name': 'Wine graph',
    'unit': 'Bottle',
    'type': 'float',
    'color': 'ajisai'
}

# graph_response = requests.post(url=graph_endpoint,
#                                 json=graph_config, 
#                                 headers=headers)

# print(graph_response.text)

#POST A PIXEL
pixel_post_config = {
    'date':datetime.now().strftime('%Y%m%d'),
    'quantity': '2'
}

pixel_post_endpoint = f'{pixela_endpoint}/{MY_USER}/graphs/{MY_GRAPHID}'

# pixel_post_response = requests.post(url=pixel_post_endpoint,
#                                 json=pixel_post_config, 
#                                 headers=headers)

# print(pixel_post_response.text)

#UPDATE A PIXEL
pixel_put_endpoint = f'{pixela_endpoint}/{MY_USER}/graphs/{MY_GRAPHID}/20221019'

pixel_put_config = {
    'quantity': '10'
}

# pixel_put_response = requests.put(url=pixel_put_endpoint,
#                                 json=pixel_put_config, 
#                                 headers=headers)

# print(pixel_put_response.text)

#DELETE A PIXEL
pixel_delete_endpoint = f'{pixela_endpoint}/{MY_USER}/graphs/{MY_GRAPHID}/20221019'


pixel_delete_response = requests.delete(url=pixel_put_endpoint, 
                                headers=headers)

print(pixel_delete_response.text)