import requests
from datetime import datetime
from pprint import pprint
from flight_data import FlightData

TEQUILA_URL = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_HEADER = {
    "apikey": "zzmW1KYJVlHkPgo6H2qD0IcnLNaih4Qj"
}
TEQUILA_PARAMS = {
    "term": "",
    "location_types": "airport",

}


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.
    # this class's purpose function is to 1) query the Tequila Flight Search API for specific flight information,
    # 2) to
    def __init__(self, sheet_data):
        self.sheet_data = sheet_data  # stores the data from the google sheet
        self.trips = {}  # stores the flight data for each destination city

    # if the data from the google sheet has a blank IATA code,
    # this function will replace the blank code with the proper IATA code
    def update_blank_iata_code(self):
        # self.sheet_data = ["TESTING" for self.sheet_data['iataCode'] in self.sheet_data if self.sheet_data['iataCode'] == '']
        # self.sheet_data = ['iataCode':'' for location['iataCode'] in self.sheet_data['sheet1']]
        for location in self.sheet_data["sheet1"]:
            iataCode = location['iataCode']
            if iataCode == '':
                location['iataCode'] = self.get_destination_code(city=location["city"])

    # designed to be used with function "update_blank_iata_code"
    # takes a String city
    # queries tequila for an IATA code for a city
    # returns the IATA code for parameter city
    def get_destination_code(self, city):
        global TEQUILA_URL
        global TEQUILA_PARAMS
        global TEQUILA_HEADER

        TEQUILA_PARAMS["term"] = city

        tequila_request = requests.get(url=TEQUILA_URL, params=TEQUILA_PARAMS,
                                       headers=TEQUILA_HEADER)
        results = tequila_request.json()["locations"]
        city_code = results[0]["code"]
        return city_code

    # updates the sheet data object with the lowest priced flights
    # takes a String departure, which is the departure city
    def query_for_listed_cities(self, departure):

        for location in self.sheet_data["sheet1"]:
            iata_code = location['iataCode']
            lowest_price_from_tequila = self.query_for_specific_flight(departure, iata_code)
            if lowest_price_from_tequila is not None and location["lowestPrice"] > lowest_price_from_tequila:
                location["lowestPrice"] = lowest_price_from_tequila
            elif lowest_price_from_tequila is None:
                location["lowestPrice"] = "NONE FOUND"

    # designed to work with function "query_for_listed_cities"
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
                          "curr": "USD",
                          "one_for_city": 1,
                          }

        tequila_url = "https://tequila-api.kiwi.com/v2/search"

        tequila_request = requests.get(url=tequila_url, params=tequila_params, headers=tequila_header)
        response = tequila_request.json()

        try:
            data = response["data"]
            return_date = response["data"][0]['route'][1]['local_departure']
        except KeyError and IndexError:
            print(f"No flights were found for {departure} to {destination} with no stopovers; "
                  f"checking for flights with one stopover...")
            # Ensure that departure airport IATA is correct.

            tequila_params = {"fly_from": departure,
                              "fly_to": destination,
                              "date_from": datetime.now().strftime("%d/%m/%Y"),
                              "date_to": datetime.now().strftime(f"%d/{today.month + 6}/%Y"),
                              "flight_type": "round",
                              "max_stopovers": 1, #check for flights with one stopover
                              "nights_in_dst_from": 7,
                              "nights_in_dst_to": 28,
                              "curr": "USD",
                              "one_for_city": 1,
                              }

            tequila_request = requests.get(url=tequila_url, params=tequila_params, headers=tequila_header)
            response = tequila_request.json()
            try:
                data = response["data"]
                return_date = response["data"][0]['route'][1]['local_departure']
            except KeyError and IndexError:
                print(f"No flights were found from {departure} to {destination} with a single stopover.")
                return None
            else:
                response_data = response["data"]
                trip = FlightData(dep_iata=response_data[0]["cityCodeFrom"],
                                  dep_city=response_data[0]["cityFrom"],
                                  dest_iata=response_data[0]["cityCodeTo"], dest_city=response_data[0]["cityTo"],
                                  dep_date=response_data[0]['route'][0]['local_departure'],
                                  ret_date=response_data[0]['route'][1]['local_departure'],
                                  price=response["data"][0]['price'], stop_overs=0, via_city=response_data[1]["cityTo"])
                pprint(response)
                return None
        try:
            return_date = response["data"][0]['route'][1]['local_departure']
        except IndexError:
            print(f"No return flight was found within the current dates for flights from {departure} to {destination}.")
            return None
        else:
            response_data = response["data"]
            trip = FlightData(dep_iata=response_data[0]["cityCodeFrom"],
                              dep_city=response_data[0]["cityFrom"],
                              dest_iata=response_data[0]["cityCodeTo"],
                              dest_city=response_data[0]["cityTo"],
                              dep_date=response_data[0]['route'][0]['local_departure'],
                              ret_date=response_data[0]['route'][1]['local_departure'],
                              price=response["data"][0]['price'])

            self.trips[destination] = trip
            #pprint(response)
            return response["data"][0]['price']

    # price, dep_iata, dest_iata, dest_city, dep_city, dep_date, ret_date, stop_overs = 0,
    # via_city = ""
    # returns the sheet data object
    def return_sheet_data(self):
        return self.sheet_data

    # returns the flight data object
    def return_trips(self):
        return self.trips
