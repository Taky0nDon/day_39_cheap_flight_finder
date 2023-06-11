import os
import requests
import datetime
# This class is response for talking to the flight search API
class FlightSearch:
    def __init__(self, destination: str | None = None):
        """

        :param destination: default value of None for methods that don't require a destination.
        """
        self.now = datetime.datetime.now()
        self.date_start = self.now.strftime("%d/%m/%Y")
        self.date_end = self.now.strftime(f"%d/{self.get_future_month()}/%Y")
        self.depart = "RDU"
        self.destination = destination
        self.endpoint = os.environ.get("FLIGHT_SEARCH_ENDPOINT")
        self.header = {"apikey": f"{os.environ.get('FLIGHT_SEARCH_KEY')}",
                       "accept": "application/json"}
        self.parameters = {
            "fly_from": self.depart,
            "fly_to": "destination",
            "dateFrom": self.date_start,
            "dateTo": self.date_end,
            "curr": "USD",
            "sort": "price",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0
        }
        self.results = self.get_flight_data()

    def get_city_code(self, term: str) -> str:
        """

        :param term:
        :return:
        """
        endpoint = f"https://{self.endpoint}/locations/query"
        parameters = {
            "term": term,
            "locale": "en-US",
            "location_types": "city",
            "active_only": "true"
        }
        response = requests.get(url=endpoint, headers=self.header, params=parameters)
        response.raise_for_status()
        city_code = response.json()["locations"][0]["code"]
        return city_code

    def get_flight_data(self) -> dict:
        self.parameters["fly_to"] = self.destination
        response = requests.get(url=f"https://{self.endpoint}/v2/search", params=self.parameters, headers=self.header)
        return response.json()

    def get_future_month(self):
        now = datetime.datetime.now()
        six_months_from_now = now.month + 6
        if six_months_from_now > 12:
            six_months_from_now %= 12
        return six_months_from_now
