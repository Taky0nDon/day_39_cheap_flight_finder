from new_data_manager import DataManager

spreadsheet = DataManager(spreadsheet_name="Copy of Flight Deals",
                          worksheet_name="User Info")
worksheet = spreadsheet.get_worksheet()

user_first_name = input("Enter your first name:\n")  # "A"
user_last_name = input("Enter your last name: \n")  # "B"
user_email = input("Enter your email address: \n")  # "C"
user_email_validation = input("Enter your email address: \n")

# You have to add two to the length of get_all_records because the first row to edit has an id of
# 2, so when the len of spreadsheet.rows is 0, you need to edit row 2, when it is one, you need to edit
# row 3, etc...
row_to_edit = len(spreadsheet.rows) + 2

if user_email == user_email_validation:
    inputs = [user_first_name, user_last_name, user_email, row_to_edit]
    print("Welcome to the flight club.")
    for column_name, input in zip(spreadsheet.columns.keys(), inputs):

        spreadsheet.edit_row(column_header=column_name, row_to_edit=row_to_edit, new_value=input)