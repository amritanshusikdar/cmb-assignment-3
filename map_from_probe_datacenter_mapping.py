'''
This file is used to create a map from the probe to data center mappings in order to find errors in the mappings and to
visualize this mapping for documentation purpose.

It reads the probe_datacenter_mapping.csv file containing ,probe_id,data_center_url,IP
'''

import pandas as pd
import folium

data = pd.read_csv('data/probe_datacenter_mapping.csv')

# Center map
m = folium.Map(location=[20,0], zoom_start=5)

# Add markers for probes and data centers
for index, row in data.iterrows():
    folium.Marker(
        location=[row['probe latitude'], row['probe longitude']],
        popup=row['probe_id'],
        icon=folium.Icon(color='blue', icon='map-marker')
    ).add_to(m)

    folium.Marker(
        location=[row['data center latitude'], row['data center longitude']],
        popup=row['data_center_url'],
        icon=folium.Icon(color='red', icon='map-marker')
    ).add_to(m)

    # Draw lines
    folium.PolyLine(
        locations=[
            [row['probe latitude'], row['probe longitude']],
            [row['data center latitude'], row['data center longitude']]
        ],
        color='black'
    ).add_to(m)

# Save map
m.save('maps/probe_datacenter_mapping_map.html')
