import time
import os
import json

import cloudconvert

CREDENTIAL_FILE = '../credentials/cloud_convert.json'

class CloudConvert():
    def __init__(self):
        self._service = cloudconvert.Api(api_key=self.get_credentials())

    def get_credentials(self):
        """Read API key from file and return it"""
        with open(CREDENTIAL_FILE) as credentials:
            data = json.load(credentials)
            api_key = data['API_KEY']

        return api_key

    def convert_url_to_pdf(self, url):
        process = self._service.convert({
            'inputformat': 'website',
            'outputformat': 'pdf',
            'input': 'url',
            'file': url
        })
        process.wait()

        file_name = '../data/cc_download_{0}.pdf'.format(time.time())
        process.download(localfile=file_name)

        return file_name

    def delete_file(self, file):
        os.remove(file)

def main():
    cc_instance = CloudConvert()
    cc_instance.convert_url_to_pdf('https://www.howtographql.com/basics/0-introduction/')

if __name__ == '__main__':
    main()