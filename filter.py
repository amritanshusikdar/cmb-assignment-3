# usage:
#   python3 filter.py [FILTERS]
#   
#   A filter can be composed with the 2 logic expressions & and | as follows:
#    - two tags in quotes form an & condition   
#    - multiple strings quoted form an | condition
#
# example:
#   python3 filter.py "home system-ipv4-stable-1d"
#   will filter out all the probes which have both of the tags
#
#   python3 filter.py "home system-ipv4-stable-1d" "wi-fi"
#   will filter out all the probes which have both the 'home' and 'system-ipv4-stable-1d' tags or those which have the 'wi-fi' tag


from json import loads
import sys

with open("20240131.json", 'r') as f:
    probes = loads(f.read())


def apply_filter(filters: list):
    ret = {}
    filters_set = set(filters)
    for key, values in enumerate(probes["objects"]):
        if filters_set.issubset(set(values["tags"])):
            ret[key] = values
    return ret

def get_ids_list(dic):
    ret = []
    for key, values in dic.items():
        ret.append(values['id'])
    return ret

tags_list = sys.argv[1:]
if tags_list == []:
    tags_list = ["home"]

if "-h" in tags_list or "--help" in tags_list:
    print("""usage: \
            \n\tpython3 filter.py [FILTERS] \
            \n\n\tA filter can be composed with the 2 logic expressions & and | as follows: \
            \n\t - two tags in quotes form an & condition  \
            \n\t - multiple strings quoted form an | condition \
            \n\nexample: \
            \n\tpython3 filter.py \"home system-ipv4-stable-1d\" \
            \n\twill filter out all the probes which have both of the tags \
            \n\n\tpython3 filter.py \"home system-ipv4-stable-1d\" \"wi-fi\" \
            \n\twill filter out all the probes which have both the 'home' and 'system-ipv4-stable-1d' tags or those which have the 'wi-fi' tag""")
else:
    ids_set = set()
    for tags in tags_list:
        filter = tags.split(' ')
        ids = get_ids_list(apply_filter(filter))
        ids_set = ids_set.union(set(ids))
    ids_list = sorted(list(ids_set))
    filter_str = '" "'.join(tags_list)
    print(f"{len(ids_list)} results for the filter \"{filter_str}\":")
    print(ids_list)
