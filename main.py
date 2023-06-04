# This file will need to use the
# DataManager,
# FlightSearch,
# FlightData,
# NotificationManager
# classes to
# achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
import json

search = FlightSearch()
results = search.get_flight_data(destination="NYC")
with open("flight_search_response.json", "w") as file:
    json.dump(results, file, indent=2)
# data = FlightData(search_results=results)
# pretty_result = json.dumps(results, indent=2)
# for result in results["data"]:
#     print(result["price"])
# print(data.earliest_flight, data.last_flight)

# for row in sheet["prices"]:
#     id = row["id"]
#     city = row["city"]
#     code = search.get_city_code(city)
#     data_manager.edit_row(row_to_edit=id, new_value=code)

# data_manager.edit_row("2", "PAR")

# search.get_city_code("paris")
# print(search.header, search.endpoint)