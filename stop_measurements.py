"""
This script is used to call RIPE ATLAS API
to stop the measurements, that corresponds to
the given measurement ID range (e.g. from FIRST_ID to LAST_ID)
"""

import requests

API_KEY = "your_API_key"

FIRST_ID = 0 #your first measurement id
LAST_ID = 1 #your last measurement id
LAST_ID += 1 # for loop below will iterate until LAST_ID (included)

for i in range(FIRST_ID, LAST_ID):
    req = requests.delete(f"https://atlas.ripe.net/api/v2/measurements/{i}", headers={"Authorization": f"Key {API_KEY}"})
    print(req.text)