import time
import json
import pocket

CREDENTIAL_FILE = '../credentials/pocket.json'

class Pocket():
    def __init__(self):
        self._service = pocket.Pocket(*self.get_credentials())

    def get_credentials(self):
        """Load API key and token from file, then return them"""
        with open(CREDENTIAL_FILE) as credentials:
            data = json.load(credentials)
            consumer_key = data['CONSUMER_KEY']
            access_token = data['ACCESS_TOKEN']

        return consumer_key, access_token

    def get_pockets(self, count=100, tag=None, recent=False):
        """Get a list of saved pockets based on given arguments"""
        from_time = time.time() - 60 if recent else None
        pocket_response = self._service.get(count=count, tag=tag, since=from_time)[0]
        pockets = list(pocket_response['list'].values())[0] if pocket_response['list'] else []

        return pockets

def main():
    pocket_instance = Pocket()
    pockets = pocket_instance.get_pockets(tag='agriculture', recent=False)
    print(pockets)

if __name__ == '__main__':
    main()