# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from api.CloudConvert import CloudConvert
from api.GoogleDrive import GoogleDrive
from api.Pocket import Pocket

def format_file_name(name):
    return ''.join(e for e in name if e.isalnum())

def main():
    pocket_instance = Pocket()
    cc_instance = CloudConvert()
    drive_instance = GoogleDrive()

    pockets = pocket_instance.get_pockets(tag='convert', recent=False)

    for pocket in pockets:
        file_name = '{0}.pdf'.format(format_file_name(pocket['resolved_title']))
        # only convert if file doesn't exist in drive
        if(not drive_instance.file_exits(file_name)):
            converted_file = cc_instance.convert_url_to_pdf(pocket['given_url'])

            file_to_upload = {
                'full_path': '../data/{0}'.format(converted_file),
                'name': file_name
            }

            drive_instance.upload_to_folder(file_to_upload, 'Unprocessed')
            cc_instance.delete_file(file_to_upload['full_path'])

if __name__ == '__main__':
    main()
