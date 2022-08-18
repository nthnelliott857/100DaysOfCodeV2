import requests
from twilio.rest import Client
from flight_data import FlightData
import smtplib

ACCOUNT_SID = "AC92b7d82fd44be3edb7e4ad6c8383d162"
AUTH_TOKEN = "4285b1a12a6fc45567ec055552bcc6cc"
TWILIO_VERIFIED_NUMBER = '+19124556582'


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, sheet_data, trips):
        self.sheet_data = sheet_data
        self.trips = trips

    # texts the contents of trips to the destination phone number
    def send_messages(self):
        for location in self.trips:
            dep_city = self.trips[location].dep_city
            dep_iata = self.trips[location].dep_iata
            dest_city = self.trips[location].dest_city
            dest_iata = self.trips[location].dest_iata
            dep_date = self.trips[location].dep_date
            ret_date = self.trips[location].ret_date
            price = self.trips[location].price
            dep_date = dep_date.split('T')[0]
            dep_date = dep_date[6:10:] + "-" + dep_date[0:4:]
            ret_date = ret_date.split('T')[0]
            ret_date = ret_date[6:10:] + "-" + ret_date[0:4:]
            stop_over = self.trips[location].stop_overs
            via_city = self.trips[location].via_city

            self.send_message(price=price, dep_city=dep_city, dep_iata=dep_iata, dest_city=dest_city,
                              dest_iata=dest_iata, dep_date=dep_date, return_date=ret_date, stop_over=stop_over, via_city=via_city)

            # iataCode = location['iataCode']

    # sends a text message to the designated phone number
    # takes parameters int price, str dep_city, str dep_iata, str dest_city,
    # str dest_iata, str dep_date, str return_date, int stop_over, str via_city
    # prints the status of the message transmission to the console
    def send_message(self, price, dep_city, dep_iata, dest_city, dest_iata, dep_date, return_date, stop_over, via_city):
        # first_three_articles_basic_info = [{"title": article["title"], "description": article["description"]} for
        #                                    article in first_three_articles]
        # print(first_three_articles_basic_info)
        global AUTH_TOKEN
        global ACCOUNT_SID

        if stop_over == 0:

            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages \
                .create(
                body=f"LOW PRICE FLIGHT ALERT: \n"
                     f"It's only ${price} to fly from \n"
                     f"{dep_city} ({dep_iata}) to {dest_city} ({dest_iata}) \n"
                     f"from {dep_date} to {return_date}! ",
                from_=TWILIO_VERIFIED_NUMBER,
                to='+15096680216'
            )
            print(message.status)
        else:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages \
                .create(
                body=f"LOW PRICE FLIGHT ALERT: \n"
                     f"It's only ${price} to fly from \n"
                     f"{dep_city} ({dep_iata}) to {dest_city} ({dest_iata}) \n"
                     f"from {dep_date} to {return_date}! \n"
                     f"Flight has {stop_over} stop over, via {via_city}.",
                from_=TWILIO_VERIFIED_NUMBER,
                to='+15096680216'
            )
            print(message.status)

    # sends emails to the email addresses in the google sheet
    def send_emails(self):

        # procures google sheet data
        sheety_headers = {
            "Authorization": "Basic bnVsbDpudWxs"
        }

        sheety_url = f"https://api.sheety.co/90ddc89a6db19a0cfd5036b2a5fc37fe/flightDeals/sheet2"
        sheety_request = requests.get(url=sheety_url, headers=sheety_headers)
        sheet_data = sheety_request.json()
        message = self.generate_email_text()
        for recipient in sheet_data["sheet2"]:
            email = recipient["email"]
            self.send_email(destination_email=email, message=message)

    # sends an individual email to a destination address
    # take a str destination email and a str message
    def send_email(self, destination_email, message):
        # info for SMTP process
        my_email = "natedoggg109312@gmail.com"
        my_password = "HorseDartNinjaPilot#6"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=destination_email, msg=message)
            #print(message.)
    #
    # returns the text of the email
    def generate_email_text(self):
        message = "Subject: LOW PRICE FLIGHT ALERT\n"
        for trip in self.trips:

            #https://www.google.co.uk/flights?hl=en#flt=STN.SXF.2020-08-25*SXF.STN.2020-09-08

            trip_data = f"It's only ${self.trips[trip].price} to fly from \n" \
                        f"{self.trips[trip].dep_city} ({self.trips[trip].dep_iata}) to {self.trips[trip].dest_city} ({self.trips[trip].dest_iata}) \n" \
                        f"from {self.trips[trip].dep_date} to {self.trips[trip].ret_date}! \n" \
                        f"Here's a link: https://www.google.co.uk/flights?hl=en#flt={self.trips[trip].dep_iata}.{self.trips[trip].dest_iata}.{self.trips[trip].dep_date}*{self.trips[trip].dest_iata}.{self.trips[trip].dep_iata}.{self.trips[trip].ret_date}"
# link = f"https://www.google.co.uk/flights?hl=en#flt={self.trips[trip].dep_iata}.{self.trips[trip].dest_iata}.{self.trips[trip].dep_date}*{self.trips[trip].dest_iata}.{self.trips[trip].dep_iata}.{self.trips[trip].ret_date}"
            if self.trips[trip].stop_overs > 0:
                trip_data += f"\nThis trip has {self.trips[trip].stop_overs} stop over(s) in {self.trips[trip].via_city}."
            message += trip_data + "\n\n"
        print(message)
        return message
