import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
spreadsheet_id = "18OlJOWQ0hRnsyKQxNSxf4MQdI7tD_SiCFm0KJLNqs84"

def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", scopes)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
            credentials = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        for row in range(2, 11):
            num1 = int(sheets.values().get(spreadsheetId=spreadsheet_id, range=f"Sheet1!A{row}").execute().get("values")[0][0])
            num2 = int(sheets.values().get(spreadsheetId=spreadsheet_id, range=f"Sheet1!B{row}").execute().get("values")[0][0])
            calc_res = num1 * num2
            print(f"Processing {num1} * {num2}")

            sheets.values().update(spreadsheetId=spreadsheet_id, range=f"Sheet1!C{row}",
                                   valueInputOption="USER_ENTERED", body={"values": [[f"{calc_res}"]]}).execute()

            sheets.values().update(spreadsheetId=spreadsheet_id, range=f"Sheet1!D{row}",
                                   valueInputOption="USER_ENTERED", body={"values": [["done"]]}).execute()

    except HttpError as error:
        print(error)

if __name__ == "__main__":
    main()
