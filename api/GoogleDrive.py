import string

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive'
FOLDER_MIME_TYPE = 'application/vnd.google-apps.folder'
CREDENTIAL_FILE = '../credentials/google_drive.json'

class GoogleDrive():
    def __init__(self):
        self._service = self.authenticate()

    def authenticate(self):
        """Authenticate using Client ID"""
        store = file.Storage('credentials.json')
        creds = store.get()

        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(CREDENTIAL_FILE, SCOPES)
            creds = tools.run_flow(flow, store)

        return build('drive', 'v3', http=creds.authorize(Http()))

    def get_files(self, options, num_files=100):
        """Return a list of files from the drive filtered by options."""
        files = []
        query = self.build_query_string(options)

        results = self._service.files().list(
            pageSize=num_files, 
            fields='nextPageToken, files(id, name)',
            q=query).execute()

        files = results.get('files', [])

        return files

    def get_folder_id(self, folder_name):
        """Returns id of folder with given name"""
        query = self.build_query_string({
            'mimeType': ['=', FOLDER_MIME_TYPE],
            'name': ['=', folder_name]
        })

        result = self._service.files().list(
            pageSize=1,
            fields='files(id)',
            q=query
        ).execute()
        
        id_container = result.get('files', [])

        return id_container[0]['id'] if id else -1

    def get_files_in_folder(self, folder_name):
        """Return all of the files in a given folder"""
        folder_id = self.get_folder_id(folder_name)
        options = { 'parents': ['in', folder_id] }
        return self.get_files(options) if folder_id != -1 else []

    def upload_to_folder(self, file, folder_name):
        """Uploads a file to the give folder"""
        file_metadata = { 
            'name': file['name'], 
            'parents':[self.get_folder_id(folder_name)]
        }

        media = MediaFileUpload(file['full_path'])

        result = self._service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        return result
    
    def build_query_string(self, options):
        """Return a string that is used to query results"""
        query_statements = []
        
        for field, params in options.items():
            op, value = params
            query_statements.append("{0} {1} '{2}'".format(field, op, value))

        query_string = " and ".join(query_statements)

        return query_string
            
def main():
    drive_instance = GoogleDrive()
    files = drive_instance.get_files_in_folder('Family')
    
    file_to_upload = {
        'full_path': '../data/test.txt',
        'name': 'test.txt'
    }

    result = drive_instance.upload_to_folder(file_to_upload, 'Unprocessed')

if __name__ == '__main__':
    main()