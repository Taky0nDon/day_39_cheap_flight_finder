import os

from twilio.rest import Client

from flight_data import FlightData

class NotificationManager:
    def __init__(self) -> None:
        self.account_sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_TOKEN")
        self.sender = os.environ.get("TWILIO_SEND")
        self.recipient = os.environ.get("TWILIO_TO")
        self.client = Client(self.account_sid, self.token)

    def send_message(self, text) -> None:
        message = self.client.messages.create(
            to=self.recipient, from_=self.sender,
            body=text
        )

    def create_message(self, flight: FlightData) -> str:
        message = f"Low price alert! Only ${flight.price} " \
                  f"to fly from {flight.city_from}-{flight.depart_from} " \
                  f"to {flight.city_to}-{flight.destination} " \
                  f"from {flight.depart_date} to {flight.return_date}"
        return message