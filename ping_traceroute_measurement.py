"""
This script is used to call RIPE ATLAS CLI Tools
to start the "ping" and "traceroute" measurements
"""

import pandas as pd
import subprocess

def run_ripe_atlas_ping(target_ip, probe_list):
    # Construct the command
    command = ["ripe-atlas", "measure", "ping", "--target", target_ip, "--from-probes", probe_list, "--interval", "7200"]
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print("Measurement successfully initiated.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Measurement initiation failed.")

def run_ripe_atlas_traceroute(target_ip, probe_list):
    # Construct the command
    command = ["ripe-atlas", "measure", "traceroute", "--target", target_ip, "--from-probes", probe_list]
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print("Measurement successfully initiated.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Measurement initiation failed.")

def list_to_string(lst):
    result = ""
    for i in range(len(lst)):
        result += str(lst[i])
        if i != len(lst) - 1:
            result += ","
    return result

def remove_first_last(string):
    if len(string) <= 2:
        return ""  # If the string has 2 or fewer characters, removing first and last will make it empty
    else:
        return string[1:-1]
    
# Example usage
if __name__ == "__main__":
    # Read the input CSV file
    df = pd.read_csv('data/datacenter_probe_mapping.csv')
    
    # run_ripe_atlas_ping("99.78.176.246", "50941")
    # run_ripe_atlas_traceroute("99.78.176.246", "50941")

    # Iterate over each row in the DataFrame to start ping measurements
    for index, row in df.iterrows():
        target_ip = row['IP']
        probe_id_list = remove_first_last(row['probe_id'])
        run_ripe_atlas_ping(target_ip, probe_id_list)
    
    # Iterate over each row in the DataFrame to start traceroute measurements
    for index, row in df.iterrows():
        target_ip = row['IP']
        probe_id_list = remove_first_last(row['probe_id'])
        run_ripe_atlas_traceroute(target_ip, probe_id_list)

