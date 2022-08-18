# from datetime import datetime
#
# today = datetime.now()
# print(today)
# print()
# #print(today.strftime("%Y%m%d"))
# print(today.strftime("%m/%d/%Y"))
# month_now = today.month
# print(month_now + 6)
# print(today.strftime(f"{today.month + 6}/%d/%Y"))

def query_for_listed_cities(self, departure):
    for location in self.sheet_data["sheet1"]:
        iata_code = location['iataCode']
        # new_flight_data_object = FlightData(price=self.query_for_specific_flight(departure, iata_code),
        #                                     departure_airport_code=departure, destination_airport_code=iata_code)
        self.flight_data[iata_code] = self.query_for_specific_flight(departure, iata_code)


def query_for_specific_flight(self, departure, destination):
    # global TEQUILA_HEADER
    today = datetime.now()
    tequila_header = {
        "apikey": "z7TXtAeZAlkHAFctag3xOKXaE-FNqQxQ"
    }

    tequila_params = {"fly_from": departure,
                      "fly_to": destination,
                      "date_from": datetime.now().strftime("%d/%m/%Y"),
                      "date_to": datetime.now().strftime(f"%d/{today.month + 6}/%Y"),
                      "flight_type": "round",
                      "max_stopovers": 0,
                      "nights_in_dst_from": 7,
                      "nights_in_dst_to": 28,
                      "curr": "GBP",
                      "one_for_city": 1,
                      }

    tequila_url = "https://tequila-api.kiwi.com/v2/search"

    tequila_request = requests.get(url=tequila_url, params=tequila_params, headers=tequila_header)
    response = tequila_request.json()
    return response["data"][0]['price']
    # pprint(response)
    # print(response["data"][0]['price'])
    # print(tequila_request.json())

    # for location in self.sheet_data["sheet1"]:
    #     city = location["city"]
    #     TEQUILA_PARAMS["term"] = city