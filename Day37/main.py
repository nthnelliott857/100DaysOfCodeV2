import requests
from datetime import datetime

USERNAME = "natedogg"
TOKEN = "ajsua2llsk4zms33oqusl"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": "ajsua2llsk4zms33oqusl",
    "username": "natedogg",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Personal_Growth_Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}


today = datetime.now()
# today = datetime(year=2020, month=2, day=15)
print(today.strftime("%Y%m%d"))
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)


add_pixel_for_today = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
add_pixel_for_today_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(input("How many days? ")),
}

# edit_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# edit_graph_config = {
#     "unit": "days"
# }

# response = requests.put(url=edit_graph, json=edit_graph_config, headers=headers)
# print(response.text)

response = requests.post(url=add_pixel_for_today, json=add_pixel_for_today_config, headers=headers)
print(response.text)

edit_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
edit_pixel_config = {
    "quantity": "45"
}

# response = requests.put(url=edit_pixel, json=edit_pixel_config, headers=headers)
# print(response.text)

delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel, headers=headers)
# print(response.text)