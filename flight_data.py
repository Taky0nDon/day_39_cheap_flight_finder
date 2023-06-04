class FlightData():
    def __init__(self, search_results: dict):
        self.flight: dict = search_results["data"][0]
        self.price: int = self.flight["price"]
        self.depart_date = self.flight["route"][0]["local_departure"].split("T")[0]
        self.return_date = self.flight["route"][1]["local_departure"].split("T")[0]
        self.depart_from = self.flight["flyFrom"]
        self.destination = self.flight["flyTo"]
