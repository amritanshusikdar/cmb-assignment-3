from json import loads


with open("data/20240131.json", 'r') as f:
    probes = loads(f.read())

tags = {}
for key, values in enumerate(probes["objects"]):
    for tag in values["tags"]:
        if tag not in tags.keys():
            tags[tag] = 1
        else:
            tags[tag] += 1

print(f"{len(tags.keys())} different tags found")
with open("data/tags_list.csv", "w") as f:
    for tag in sorted(tags, key=tags.get, reverse=True):
        f.write(f"{tag},{tags[tag]}\n")
print("File created")

