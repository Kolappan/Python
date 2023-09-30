import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from extract_msg import Message

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
            return items
    except HttpError as error:
        print(f"An error occurred: {error}")
        items = None

    return items

def download_file(file_id, file_name, output_directory):
    try:
        service = build('drive', 'v3', credentials=credentials)
        request = service.files().get_media(fileId=file_id)
        file_path = os.path.join(output_directory, file_name)

        with open(file_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f'Download progress: {int(status.progress() * 100)}.')
        return file_path

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def upload_file(file_path, file_name, folder_id):
    try:
        service = build('drive', 'v3', credentials=credentials)
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path, resumable=True)

        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File ID: {file.get('id')}")

    except HttpError as error:
        print(f"An error occurred: {error}")


# ----- .msg to .txt conversion functions -----

def msg_to_txt(input_file, output_file):
    msg = Message(input_file)
    body = msg.body

    with open(output_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(body)

    print(f'Successfully saved email body from {input_file} to: {output_file}')


# ----- Main script -----

input_folder_id = '13GXbEn8Y8nz5bzhxjHfkML84Oj5WBf8L'
output_folder_id = '1CXtq49o17Uiv0axpWw-tfieXuos7E1xN'

input_directory = 'msgFiles'
output_directory = 'outText'

os.makedirs(input_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

files = list_files_in_folder(input_folder_id)

if files:
    for file in files:
        if file['mimeType'] == 'application/vnd.ms-outlook' and file['name'].endswith('.msg'):
            local_msg_path = download_file(file['id'], file['name'], input_directory)
            local_txt_path = os.path.join(output_directory, file['name'].replace('.msg', '.txt'))
            msg_to_txt(local_msg_path, local_txt_path)
            upload_file(local_txt_path, file['name'].replace('.msg', '.txt'), output_folder_id)