'''
This script will map probes to datacenters by the continent that they are located in.
The script reads two files:
- The mapping of the data centers to their continent: url,target_ip,longitude,latitude
- The mapping of the probes to their continent: probe_id,type,latitude,longitude,continent
'''

import pandas as pd

# Open files
df_probes = pd.read_csv('data/coordinates_continents_selected_probes.csv')
df_endpoints = pd.read_csv('data/endpoints.csv')

# Create mapping between data centers and probes and output csv file
df_combined = df_probes.merge(df_endpoints, on='continent')

df_combined.to_csv('data/probe_datacenter_mapping.csv')

