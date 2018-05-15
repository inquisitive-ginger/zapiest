# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from api.CloudConvert import CloudConvert
from api.GoogleDrive import GoogleDrive
from api.Pocket import Pocket

pocket_instance = Pocket()
cc_instance = CloudConvert()
drive_instance = GoogleDrive()

pockets = pocket_instance.get_pockets(tag='convert', recent=True)

for pocket in pockets:
    converted_file = cc_instance.convert_url_to_pdf(pocket['given_url'])
    file_name = pocket['resolved_title']

    file_to_upload = {
        'full_path': '../data/{0}'.format(converted_file),
        'name': file_name
    }

    drive_instance.upload_to_folder(file_to_upload, 'Unprocessed')
    cc_instance.delete_file(file_to_upload['full_path'])
