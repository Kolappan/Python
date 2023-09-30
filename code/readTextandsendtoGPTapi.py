import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload


# ----- Google Drive API setup and functions -----

SERVICE_ACCOUNT_FILE = 'GdriveRead.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

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
            return items
    except HttpError as error:
        print(f"An error occurred: {error}")
        items = None

    return items

# Read the file contents
def read_file_content(fileId):
    file_id = file['id']
    # Get the file content
    file_content = drive_service.files().get_media(fileId=file_id).execute()
    return file_content


# ----- Main script -----

input_folder_id = '1CXtq49o17Uiv0axpWw-tfieXuos7E1xN'
# output_folder_id = '1CXtq49o17Uiv0axpWw-tfieXuos7E1xN'
drive_service = build('drive', 'v3', credentials=credentials)

# Get a list of files in the input folder
files = list_files_in_folder(input_folder_id)

# Read the files and send them to the GPT-3 API
for file in files:
    file_content = read_file_content(file['id'])
    print(file_content.decode())


    



