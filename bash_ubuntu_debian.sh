#!/bin/bash

# Update package index
sudo apt-get update && sudo apt-get upgrade -y

# Install Python 3 if not already installed
sudo apt-get install -y python3

# Install pip for Python 3 if not already installed
sudo apt-get install -y python3-pip

# Use pip to install required Python packages
sudo -H pip3 install pandas numpy scikit-learn folium haversine geoip2 requests tqdm
