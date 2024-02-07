'''
This script will map probes to datacenters located near them.

There are two rules for connecting nodes and data centers:
1. It will try to connect every probe to every data center in its own country.
2. It will also connect a node to every data center inside a radius of 2000 kilometers.

The script reads two files:
- The mapping of the data centers to their continent: url,target_ip,longitude,latitude,country
- The mapping of the probes to their continent: probe_id,type,latitude,longitude,continent,country code
'''

import pandas as pd
from haversine import haversine

# Open files
df_probes = pd.read_csv('data/coordinates_continents_selected_probes.csv')
df_endpoints = pd.read_csv('data/datacenters_with_country_code.csv')


mappings = []

# Iterate through all the nodes
for probe_index, probe in df_probes.iterrows():
    probe_country = probe['country code']
    probe_lat = probe['latitude']
    probe_lon = probe['longitude']

    # Iterate through all the data centers
    for dc_index, data_center in df_endpoints.iterrows():
        dc_country = data_center['country code']
        dc_lat = data_center['latitude']
        dc_lon = data_center['longitude']

        # Calculate the distance between the nodes
        distance = haversine((probe_lat,probe_lon), (dc_lat,dc_lon))

        # 1. Same country
        if probe_country == dc_country:
            mappings.append((probe['id'], data_center['URL'], data_center['IP']))

        # 2. Within 2000 km radius
        elif distance <= 2000:
            mappings.append((probe['id'], data_center['URL'], data_center['IP']))

df_combined = pd.DataFrame(mappings, columns=['probe_id', 'data_center_url', 'IP'])


df_combined.to_csv('data/probe_datacenter_mapping.csv')

