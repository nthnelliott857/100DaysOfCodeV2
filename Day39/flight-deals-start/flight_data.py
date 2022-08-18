class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, dep_iata, dest_iata, dest_city, dep_city, dep_date, ret_date, stop_overs=0,
                 via_city=""):
        self.price = price
        self.dep_iata = dep_iata
        self.dest_iata = dest_iata
        self.dep_city = dep_city
        self.dest_city = dest_city
        self.dep_date = dep_date
        self.ret_date = ret_date
        self.stop_overs = stop_overs
        self.via_city = via_city

    # def return_flight_data_dictionary(self):
    #     return self.flight_data_dictionary
        # price, dep_city, dep_iata, dest_city, dest_iata, dep_date, return_date




