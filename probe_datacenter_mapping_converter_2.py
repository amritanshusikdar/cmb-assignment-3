"""
This script is used to ensure reverse mapping of
"datacenter vs probe" (instead of "probe vs datacenter") is correct
"""


import pandas as pd

# Read the input CSV file
df = pd.read_csv('data/probe_datacenter_mapping.csv')

# Group by data_center_url and IP, then aggregate probe_id into a list
grouped = df.groupby(['data_center_url', 'IP'])['probe_id'].agg(probe_id_list=lambda x: list(x), probe_id_list_length='count').reset_index()

# Add an index column
grouped['index'] = grouped.index

# Reorder columns
grouped = grouped[['index', 'data_center_url', 'IP', 'probe_id_list', 'probe_id_list_length']]

# Save the result to a new CSV file
grouped.to_csv('data/datacenter_probe_mapping_with_probe_id_count.csv', index=False)
