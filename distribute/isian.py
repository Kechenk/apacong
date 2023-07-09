import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils	import get_column_letter

scopes = ["https://www.googleapis.com/"]