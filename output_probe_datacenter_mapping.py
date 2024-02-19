'''
This script will map probes to datacenters located near them.

There are two rules for connecting nodes and data centers:
1. It will try to connect every probe to every data center in its own country as long as they are close enough.
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

        # 1. Same country. Filter distance for islands belonging to a country far away
        if probe_country == dc_country and distance <= 8000:
            mappings.append((probe['id'], data_center['URL'], data_center['IP'], probe['latitude'], probe['longitude'],
                             data_center['latitude'], data_center['longitude']))

        # 2. Within 2000 km radius
        elif distance <= 2000:
            mappings.append((probe['id'], data_center['URL'], data_center['IP'], probe['latitude'], probe['longitude'],
                             data_center['latitude'], data_center['longitude']))

df_combined = pd.DataFrame(mappings, columns=['probe_id', 'data_center_url', 'IP', 'probe latitude', 'probe longitude',
                                              'data center latitude', 'data center longitude'])

# Group by data_center_url and IP, then aggregate probe_id into a list
grouped = df_combined.groupby(['data_center_url', 'IP'])['probe_id'].apply(list).reset_index()

# Add an index column
grouped['index'] = grouped.index

# Reorder columns
grouped = grouped[['index', 'data_center_url', 'IP', 'probe_id']]

# Save the result to CSV file
grouped.to_csv('data/datacenter_probe_mapping.csv', index=False)


