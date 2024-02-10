"""
This script is used to call RIPE ATLAS CLI tools
to start the "ping" measurements
"""

import pandas as pd
import subprocess
import ast

def run_ripe_atlas_ping(target_ip, probe_list_str):
    # Construct the command
    command = ["ripe-atlas", "measure", "ping", "--target", target_ip, "--from-probes", probe_list_str, "--interval", "7200"]
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print("Measurement successfully initiated.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Measurement initiation failed.")

def remove_first_last(string):
    if len(string) <= 2:
        return ""  # If the string has 2 or fewer characters, removing first and last will make it empty
    else:
        return string[1:-1]
    
# Main function
if __name__ == "__main__":
    # Read the input CSV file
    df = pd.read_csv('data/datacenter_probe_mapping.csv')

    # Iterate over each row in the DataFrame to start ping measurements
    for index, row in df.iterrows():
        target_ip = row['IP']

        probe_id_list_str = row['probe_id']
        probe_id_list = ast.literal_eval(probe_id_list_str)

        tens = len(probe_id_list) // 100
        tens += 1

        for i in range(tens):
            sub_probe_id_list = probe_id_list[i * 100 : (i+1)*100]
            sub_probe_id_list_str = remove_first_last(str(sub_probe_id_list))

            """
            If you uncomment the part below it will run CLI commands
            to start the measurements, please use it cautiously
            """
            # run_ripe_atlas_ping(target_ip, sub_probe_id_list_str)

