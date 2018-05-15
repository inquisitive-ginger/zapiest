import json

import pocket
import cloudconvert

pocket_instance = pocket.Pocket(POCKET_CONSUMER_KEY, POCKET_ACCESS_TOKEN)
cc_instance = cloudconvert.Api(CLOUD_CONVERT_API_KEY)

pocket_response = pocket_instance.get(count=1)[0]
pocket_entry = list(pocket_response['list'].values())[0]
entry_url = pocket_entry['given_url']

process = cc_instance.convert({
    "inputformat": "website",
    "outputformat": "pdf",
    "input": "url",
    "file": entry_url,
    "output": "googledrive"
})
process.wait()
print(entry_url)
