import sys
sys.path.append('../api/')

from Pocket import Pocket
from CloudConvert import CloudConvert
from GoogleDrive import GoogleDrive

pocket_service = Pocket()
cc_service = CloudConvert()
drive_service = GoogleDrive()

pockets = pocket_service.get_pockets()