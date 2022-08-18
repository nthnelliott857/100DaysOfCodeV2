# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

# the URL of the sheet document
sheety_url = "https://api.sheety.co/90ddc89a6db19a0cfd5036b2a5fc37fe/flightDeals/sheet1"

# the authorization header to access the sheet document
sheety_headers = {
    "Authorization": "Basic bnVsbDpudWxs"
}

ORIGIN_CITY = "SEA"

#obtains city info from google sheet
sheety_request = requests.get(url=sheety_url, headers=sheety_headers)
sheet_data = sheety_request.json()
pprint(sheet_data)

#generates flight search object
flight_search = FlightSearch(sheet_data)

#fills in IATA code column with proper values
flight_search.update_blank_iata_code()
pprint(flight_search.return_sheet_data())

# queries tequila for listed flights
flight_search.query_for_listed_cities(departure=ORIGIN_CITY)
# flight_search = FlightSearch(None) # for testing purposes
# flight_search.query_for_specific_flight(departure=input("Departure City IATA: "), destination=input("Destination IATA: ")) # for testing purposes
sheet_data = flight_search.return_sheet_data()
trips = flight_search.return_trips()

# pprint(sheet_data)

##updates google sheet
if input("Update Google Sheet? Type 'y' for 'yes': ").lower() == "y":
    data_manager = DataManager(sheet_data)
    data_manager.update_google_sheet()

##sends notification texts
if input("Send notification text(s)? Type 'y' for 'yes': ").lower() == "y":
    notification_manager = NotificationManager(sheet_data=sheet_data, trips=trips)
    notification_manager.send_messages()


# testing email notification
if (input("send email update to subscribers? y/n ").lower() == "y"):
    # test trips object
    # trips = {"Phoenix": FlightData(price=220, dep_iata="SEA", dest_iata="PHX", dest_city="Phoenix", dep_city="Seattle",
    #                                dep_date="2022-05-13", ret_date="2022-05-20"),
    #          "NYC": FlightData(price=450, dep_iata="SEA", dest_iata="JFK",
    #                            dest_city="New York", dep_city="Seattle", dep_date="2022-05-16", ret_date="2022-05-29",
    #                            stop_overs=1,
    #                            via_city="Chicago"),
    #          "SFO": FlightData(price=340, dep_iata="SEA", dest_iata="SFO", dest_city="San Fransisco",
    #                            dep_city="Seattle", dep_date="2022-05-17", ret_date="2022-05-28", stop_overs=0,
    #                            via_city="")}
    # # for trip in trips:
    # #     print(trips[trip].price)

    notification_manager = NotificationManager(sheet_data=sheet_data, trips=trips)
    notification_manager.send_emails()
    #notification_manager.send_emails()
    # notification_manager.send_email("nthnelliott857@gmail.com", "Subject: TEST"
    #                                                             "This is a test.")
    #notification_manager.generate_email_text()
