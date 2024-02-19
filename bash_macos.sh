#!/bin/bash

# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Update Homebrew
brew update

# Install Python 3 if not already installed
brew install python3

# Use pip to install required Python packages
pip3 install pandas numpy scikit-learn folium haversine geoip2 requests tqdm
