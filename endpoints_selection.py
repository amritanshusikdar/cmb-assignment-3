import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import folium

df = pd.read_csv("data/datacenters.csv")

def get_location(id: int) -> (float, float):
    """Returns the location of a datacenter from its id in the list"""
    return np.array(df.loc[df['id'] == id, ["lat", "lon"]])[0]

def get_location_list(ids_list: [int]) -> [(float, float)]:
    """Returns the list of locations from a list of ids"""
    return [get_location(id) for id in ids_list]

def generate_map_file(ids_list: [int], file_name: str, colors: [str] = None):
    """Generates a map file with a given file name from the list of ids"""
    locs = get_location_list(ids_list)
    m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)
    if colors is None:
        colors = ['blue']*len(locs)
    for i in range(len(locs)):
        folium.Marker(location=locs[i], icon=folium.Icon(color=colors[i], icon='map-marker')).add_to(m)
    map_html = m._repr_html_()
    with open("maps/"+file_name+".html", 'w') as f:
        f.write(map_html)

def cluster(ids_list: [int], n: int) -> [int]:
    """Calculates n clusters of points from a given list of ids and returns the centroids of those clusters"""
    kmeans = KMeans(n_clusters=n)
    locs = get_location_list(ids_list)
    kmeans.fit(locs)
    closests, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, locs)
    return [ids_list[i] for i in closests]


colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'gray', 'cadetblue']

# generate the map file with a different color for each cloud provider
L = []
cps = df['CP'].unique()
for cp in cps:
    df_cp = df.loc[df['CP'] == cp]
    L += df_cp["id"].to_list()
colors_list = []
for i in range(len(cps)):
    colors_list += [colors[i]]*len(df.loc[df['CP'] == cps[i]])
generate_map_file(L, f"datacenters", colors=colors_list)
