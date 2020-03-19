import os
import json
import geojson
import requests
import shutil
def post_to_geoevent(json_data, geoevent_url):
    headers = {
        'Content-Type': 'application/json',
                }

    response = requests.post((geoevent_url), headers=headers, data=json_data, verify=False)

dirpath = r'E:\GeoJSON'

before = {}
# Empty counter object used to keep track of how many documents have been processed.
count = 0

while True:

    # Compares the folder contents after the sleep to what existed beforehand, and makes a list of adds and removes
    after = dict([(f, None) for f in os.listdir(doc_folder)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]

    if added: print("Added: ", ", ".join (added))
    if removed: print("Removed: ", ", ".join (removed))
    before = after

    for doc in added:

        stupid_file = os.path.join(dirpath,doc)
        try:
            with open(stupid_file, 'r') as json_file:
                data = json.load(json_file)
                url = "https://wdcrealtime.esri.com:6143/geoevent/rest/receiver/gdelt-in"
                post_to_geoevent(json.dumps(data), url)
                print("POSTed {}".format(doc))
            shutil.move(stupid_file, r"E:\completed")
        except Exception as e:
            print(e)
            shutil.move(stupid_file, r"E:\errors")