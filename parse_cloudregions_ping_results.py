from geoip import geolite2
import requests
import json
import time
from tqdm import tqdm
import pandas as pd
import numpy as np

def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        ret = json.loads(requests.get(url).text)
    except:
        return -1000, -1000
    if ret['status'] == "success":
        return ret['lat'], ret['lon']
    else:
        return -1000, -1000


with open('data/ping_results.txt', 'r') as f:
    lines = f.readlines()

L = []
for l in tqdm(lines):
    temp = l.split(': ')
    url, ip = temp[0].split(' ')[2:]
    ip = ip[1:-1]
    loc = get_location(ip)
    L.append((url, ip, loc[0], loc[1]))
    time.sleep(.8)

df = pd.read_csv('data/cloudregions.csv')

df2 = pd.DataFrame(np.array(L), columns=["URL", "IP", "latitude", "longitude"])

output = df.merge(df2, on="URL")
output.to_csv("data/datacenters.csv", sep=',')



