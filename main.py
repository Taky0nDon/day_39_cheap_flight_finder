# This file will need to use the
# DataManager,
# FlightSearch,
# FlightData,
# NotificationManager
# classes to
# achieve the program requirements.

from flight_search import FlightSearch
from new_data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import json
notifier = NotificationManager()
spreadsheet = DataManager(spreadsheet_name="Copy of Flight Deals",
                                 worksheet_name="prices")
print(spreadsheet.rows)
# spreadsheet = spreadsheet.get_spreadsheet()
# spreadsheet.add_worksheet(title="User Info", rows=10, cols=10)

flight_found = False
for row in spreadsheet.rows:
    city_code = row["city_code"]
    print(f"Search for flights to {city_code}")
    results = FlightSearch(destination=city_code).results
    try:
        data = FlightData(results)
    except IndexError:
        print(f"No flights to {row['city_code']} found!")
        continue
    if data.price <= row["Lowest Price"]:
        print(f"Cheap flight to {data.city_to} found for {data.price}!")
        column = spreadsheet.columns["Lowest Price"]
        cell = f"{column}{row['id']}"
        spreadsheet.edit_row(row_to_edit=row["id"], new_value=data.price, column_header="Lowest Price")
        print(f"Cell {cell} updated.")
        message = notifier.create_message(data)
        notifier.send_message(message)
        flight_found = True
if not flight_found:
    print("No qualifying flights found.")
