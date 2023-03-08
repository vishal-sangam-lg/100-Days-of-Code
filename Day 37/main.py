# Graph can be viewed at https://pixe.la/v1/users/vishalsangam/graphs/graph1.html

import requests
from datetime import datetime

USERNAME = "vishalsangam"
TOKEN = "mysecretkey"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# Creating a user account in pixela (one time process)
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

#########################################################

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "shibafu",
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# Creating a graph (one time process)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#########################################################

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2023, month=3, day=7)
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# Adding new entry
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

#########################################################

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "4.5"
# }

# Updating an entry
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

#########################################################

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

# Deleting an entry
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
