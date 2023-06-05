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
from notification_manager import NotificationManager
import json
notifier = NotificationManager()
spreadsheet = DataManager(sheet_name="prices")
flight_found = False
for row in spreadsheet.rows:
    print("Checking for cheap flights...")
    results = FlightSearch(destination=row["cityCode"]).results
    try:
        data = FlightData(results)
    except IndexError:
        print(f"No flights to {row['cityCode']} found!")
    if data.price <= row["lowestPrice"]:
        print(f"Cheap flight to {data.city_to} found!")
        spreadsheet.edit_row(row_to_edit=row["id"], new_value=data.price, column_header="lowestPrice")
        message = notifier.create_message(data)
        notifier.send_message(message)
        flight_found = True
        with open("flight_search_response.json", "a") as file:
            json.dump(data.flight, file, indent=2)
            file.write("next flight")
if not flight_found:
    print("No qualifying flights found.")
