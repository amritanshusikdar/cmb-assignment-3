import requests

API_KEY = "key"

FIRST_ID = 67568027
LAST_ID = 67568333
# LAST_ID = 67568028


for i in range(FIRST_ID, LAST_ID):
    req = requests.delete(f"https://atlas.ripe.net/api/v2/measurements/{i}", headers={"Authorization": f"Key {API_KEY}"})
    print(req.text)