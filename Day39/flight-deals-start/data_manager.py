import requests


#
# SHEETY_URL =
# SHEETY_INPUTS =

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_data):
        self.sheet_data = sheet_data

    # parameters:
    # updates google sheet
    def update_google_sheet(self):
        sheety_headers = {
            "Authorization": "Basic bnVsbDpudWxs"
        }

        for location in self.sheet_data["sheet1"]:
            id = location['id']
            sheety_url = f"https://api.sheety.co/90ddc89a6db19a0cfd5036b2a5fc37fe/flightDeals/sheet1/{id}"
            sheet_inputs = {
                "sheet1": {
                    "iataCode": location['iataCode'],
                    "lowestPrice": location["lowestPrice"]
                }
            }
            sheety_request = requests.put(url=sheety_url, headers=sheety_headers, json=sheet_inputs)

            #print(sheety_request.text)
