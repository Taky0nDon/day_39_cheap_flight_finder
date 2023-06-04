import os
import requests


class DataManager:
    def __init__(self):
        self.sheety_token = os.environ.get("SHEETY_TOKEN")
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.header = {"Authorization": f"Bearer {self.sheety_token}"}
        self.sheet_edit_parameters = {
            "price": {
            "iataCode": "city_code",
            }
        }

    def get_rows(self, sheet_name: str) -> list[dict]:
        """

        :param sheet_name:
        :return:
        """
        response = requests.get(url=self.sheety_endpoint, headers=self.header)
        return response.json()[sheet_name]

    def edit_row(self, row_to_edit: str, new_value: str, column_header: str) -> None:
        """

        :param row_to_edit:
        :param new_value:
        :param column_header:
        :return:
        """
        self.sheet_edit_parameters["price"][column_header] = new_value
        edit = requests.put(url=f"{self.sheety_endpoint}/{row_to_edit}",
                            headers=self.header,
                            json=self.sheet_edit_parameters)
        edit.raise_for_status()