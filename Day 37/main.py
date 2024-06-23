import requests
from datetime import datetime

TOKEN = ""
USERNAME = ""
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

'''response = requests.post(url=pixela_endpoint, json=users_params)
print(response.text)'''

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Novel Graph",
    "unit": "Chapters",
    "Type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

'''response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)'''

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_config = {
    "date": "20240622",
    "quantity": "7",
}

'''response = requests.post(url=post_pixel_endpoint, json=post_config, headers=headers)
print(response.text)'''

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "13",
}

'''response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)'''

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{post_config['date']}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)