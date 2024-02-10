"""
This script is used to call RIPE ATLAS API
to start the "traceroute" measurements
"""

import pandas as pd
import requests
from json import loads
import ast

YOUR_EMAIL = "your_email@example.com"
YOUR_API_KEY = "your_API_key"

def run_ripe_atlas_traceroute(target_ip, ids_list):
    probes = [{"type":"probes", "value": str(id), "requested": 1} for id in ids_list]
    json = {'definitions': [{'type': 'traceroute', 'af': 4, 'resolve_on_probe': True, 'description': f"Traceroute measurement to {str(target_ip)}", 'response_timeout': 4000, 'protocol': 'UDP', 'packets': 3, 'size': 48, 'first_hop': 1, 'max_hops': 32, 'paris': 16, 'destination_option_size': 0, 'hop_by_hop_option_size': 0, 'dont_fragment': False, 'skip_dns_check': False, 'target': str(target_ip)}], 'probes': probes, 'is_oneoff': True, 'bill_to': YOUR_EMAIL}

    req = requests.post("https://atlas.ripe.net/api/v2/measurements/", headers={"Authorization":f"Key {YOUR_API_KEY}"}, json=json)
    print(loads(req.text))
    return loads(req.text)["measurements"][0]


def remove_first_last(string):
    if len(string) <= 2:
        return ""  # If the string has 2 or fewer characters, removing first and last will make it empty
    else:
        return string[1:-1]
    
# Main function
if __name__ == "__main__":
    # Read the input CSV file
    df = pd.read_csv('data/datacenter_probe_mapping.csv')
    
    # Iterate over each row in the DataFrame to start traceroute measurements
    tens_list = []
    measurement_ids_list = []
    for index, row in df.iterrows():
        target_ip = row['IP']

        probe_id_list_str = row['probe_id']
        probe_id_list = ast.literal_eval(probe_id_list_str)

        tens = len(probe_id_list) // 100
        tens += 1
        tens_list.append(tens)

        """
        If you uncomment part below it will send API requests,
        please use it cautiously
        """
        # for i in range(tens):
        #     measurement_id = run_ripe_atlas_traceroute(target_ip, probe_id_list[i * 100 : (i+1)*100])
        #     measurement_ids_list.append(measurement_id)

    print(measurement_ids_list)

