import os

import gspread

class DataManager:
    def __init__(self, spreadsheet_name, worksheet_name):
        self.spreadsheet_name = spreadsheet_name
        self.worksheet_name = worksheet_name
        self.credentials = os.environ.get("SERVICE_ACCOUNT")
        self.service_account = gspread.service_account(filename=self.credentials)
        self.spreadsheet = self.get_spreadsheet()
        self.worksheet = self.get_worksheet()
        self.rows = self.worksheet.get_all_records()
        print(f"{self.rows=}")
        self.columns = self.get_column()

    def get_spreadsheet(self) -> gspread.Spreadsheet:
        return self.service_account.open(self.spreadsheet_name)

    def get_worksheet(self) -> gspread.Worksheet:
        return self.spreadsheet.worksheet(self.worksheet_name)


    def update_sheet(self) -> None:
        pass

    def get_cell_value(self, A1_cell: str) -> str:
        """ Pass in the cell ID in A1 notation, return the cell value"""
        return self.worksheet.acell(A1_cell).value

    def get_column(self) -> dict:
        """Returns a dictionary where the keys are the column names and the values are the appropriate letter
        for A1 notation. So the first column will be paired with "A", the second with "B", etc"""
        number_of_columns = 4
        cell_headers = self.rows[0].keys() if self.rows != [] else None
        # For when the column names are the only data in the spreadsheet, the dictionary is made by calling for
        # the values of the first N cells in the first row, where N is the number of columns, which is currently hard
        # coded
        if cell_headers == None:
            cell_headers = [self.get_cell_value(f"{chr(n)}1") for n in range(ord("A"), ord("A") + number_of_columns)]
        column_letter = {key:letter for key, letter in zip(cell_headers,
                                                   [chr(n) for n in range(65, 65+len(cell_headers))])
                        }
        self.columns = column_letter
        print(f"{self.columns=}")
        return column_letter

    def edit_row(self, column_header: str, row_to_edit: int, new_value: str) -> None:
        """

        :param column_header:
        :param row_to_edit:
        :param new_value:
        :return:
        """
        column_letter = self.columns[column_header]
        self.worksheet.update_acell(label=f"{column_letter}{row_to_edit}", value=new_value)