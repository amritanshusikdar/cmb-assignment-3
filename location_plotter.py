import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pycountry_convert as pc
import time

from pprint import pprint
from typing import Tuple

from tqdm import tqdm
tqdm.pandas()

from json import loads

'''
    Function code from:
    https://medium.com/bitgrit-data-science-publication/get-continent-names-from-coordinates-using-python-8560cdcfdfbb
'''
def get_continent_name(continent_code: str) -> str:
    continent_dict = {
        "NA": "North America",
        "SA": "South America",
        "AS": "Asia",
        "AF": "Africa",
        "OC": "Oceania",
        "EU": "Europe",
        "AQ" : "Antarctica"
    }
    return continent_dict[continent_code]


'''
    Get the continent for a given coordinate.
    Important: API limit of not more than 1 request per second. See: https://operations.osmfoundation.org/policies/nominatim/
    Function code from:
    https://medium.com/bitgrit-data-science-publication/get-continent-names-from-coordinates-using-python-8560cdcfdfbb
'''
def get_continent(lat: float, lon: float) -> str:
    geolocator = Nominatim(user_agent="<username>@gmail.com", timeout=10)
    geocode = RateLimiter(geolocator.reverse, min_delay_seconds=1)
    location = geocode(f"{lat}, {lon}", language="en")

    # for cases where the location is not found, coordinates are antarctica
    if location is None:
        return "Antarctica", "Antarctica"

    # extract country code
    address = location.raw["address"]
    country_code = address["country_code"].upper()

    # get continent code from country code
    continent_code = pc.country_alpha2_to_continent_code(country_code)
    continent_name = get_continent_name(continent_code)
    return continent_name

# Load CSV containing coordinats
df = pd.read_csv('coordinates.csv')

# Add continent column to the dataframe
df["continent"] = df.apply(lambda row: get_continent(row["latitude"], row["longitude"]), axis=1)

# Write the dataframe to updated csv
df.to_csv("coordinates_continents", sep='\t')

print(df["continent"].value_counts()/len(df["continent"]))