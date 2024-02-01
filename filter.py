# usage:
#   python3 filter.py [FILTERS]
#
# example:
#   python3 filter.py home system-ipv4-stable-1d


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

filters_list = sys.argv[1:]
if filters_list == []:
    filters_list = ["home"]

if "-h" in filters_list or "--help" in filters_list:
    print("""usage:\
            \n\tpython3 filter.py [FILTERS]\
            \nexample:\
            \n\tpython3 filter.py home system-ipv4-stable-1d""")
else:
    l = apply_filter(filters_list)
    print(get_ids_list(l))
