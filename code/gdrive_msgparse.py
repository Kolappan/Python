import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set the path to your JSON key file
# SERVICE_ACCOUNT_FILE = 'path/to/your/JSON-key-file.json'
SERVICE_ACCOUNT_FILE = 'GdriveRead.json'

# Define the Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate using the service account
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes= SCOPES)

def list_files_in_folder(folder_id):
    try:
        service = build('drive', 'v3', credentials=credentials)
        query = f"'{folder_id}' in parents and mimeType != 'application/vnd.google-apps.folder' and trashed = false"
        results = service.files().list(q=query, fields="nextPageToken, files(id, name, mimeType)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found in the folder.')
        else:
            print('Files:')
            for item in items:
                print(f"{item['name']} ({item['id']})")

    except HttpError as error:
        print(f"An error occurred: {error}")
        items = None

    return items

# Replace 'your_folder_id' with the ID of the folder you want to read files from
# folder_id = '1bMSax6OZxfiDjqTYclUZ7XfqEiztfGGy'
folder_id = '13GXbEn8Y8nz5bzhxjHfkML84Oj5WBf8L'
files = list_files_in_folder(folder_id)

# print(files)