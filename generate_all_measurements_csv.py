import requests
import json
import csv

filename = "data/combined_measurements.csv"

# measurement_ids = [67611408, 67611409, 67611410]


measurement_ids = [67611408, 67611409, 67611410, 67611412, 67611413, 67611414, 67611415, 67611416, 67611418, 67611419,
                   67611421, 67611423, 67611424, 67611425, 67611426, 67611427, 67611428, 67611429, 67611430, 67611431,
                   67611432, 67611433, 67611434, 67611436, 67611437, 67611438, 67611439, 67611440, 67611441, 67611442,
                   67611443, 67611444, 67611445, 67611446, 67611447, 67611448, 67611449, 67611450, 67611451, 67611452,
                   67611453, 67611454, 67611455, 67611456, 67611457, 67611459, 67611460, 67611463, 67611464, 67611465,
                   67611466, 67611467, 67611469, 67611470, 67611471, 67611472, 67611473, 67611474, 67611475, 67611476,
                   67611477, 67611478, 67611479, 67611480, 67611481, 67611482, 67611483, 67611484, 67611485, 67611486,
                   67611487, 67611490, 67611491, 67611492, 67611493, 67611494, 67611495, 67611496, 67611497, 67611498,
                   67611499, 67611500, 67611501, 67611502, 67611503, 67611504, 67611505, 67611506, 67611507, 67611508,
                   67611509, 67611510, 67611512, 67611513, 67611515, 67611516, 67611517, 67611518, 67611519, 67611520,
                   67611521, 67611522, 67611523, 67611524, 67611525, 67611526, 67611527, 67611528, 67611529, 67611530,
                   67611531, 67611532, 67611533, 67611534, 67611535, 67611536, 67611537, 67611539, 67611540, 67611541,
                   67611542, 67611543, 67611544, 67611545, 67611546, 67611547, 67611548, 67611549, 67611550, 67611551,
                   67611552, 67611553, 67611554, 67611555, 67611556, 67611558, 67611559, 67611560, 67611562, 67611563,
                   67611564, 67611566, 67611567, 67611568, 67611569, 67611570, 67611571, 67611572, 67611573, 67611574,
                   67611575, 67611576, 67611577, 67611578, 67611579, 67611580, 67611581, 67611582, 67611583, 67611584]

def get_results(measurement_id):
    return json.loads(requests.get(
        f"https://atlas.ripe.net/api/v2/measurements/{measurement_id}/results/?start=1707517546&stop=1708193932&format=json").text)


with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    header = ["rtt1", "rtt2", "rtt3", "ttl", "x", "fw", "lts", "dst_name", "af", "dst_addr", "src_addr", "proto",
              "size", "dup",
              "rcvd", "sent", "min", "max", "avg", "msm_id", "prb_id", "timestamp", "msm_name", "from", "type",
              "group_id", "step", "stored_timestamp"]
    writer.writerow(header)

    for measurement in measurement_ids:
        result = get_results(measurement)
        for r in result:
            row = []

            if "error" in r["result"][0].keys():
                print("---------ERROR ENCOUNTERED--------")
                print(r["result"])
                print("----------------------------------")

                row.extend([-2, -2, -2, -2, r["fw"], r["lts"],
                            r["dst_name"], r["af"],
                            r["dst_addr"], r["src_addr"],
                            r["proto"], r["size"], r["dup"], r["rcvd"], r["sent"], r["min"], r["max"],
                            r["avg"],
                            r["msm_id"], r["prb_id"], r["timestamp"], r["msm_name"], r["from"], r["type"],
                            r["group_id"],
                            r["step"], r["stored_timestamp"]])
                writer.writerow(row)
                continue

            count = 0
            for rtt in r["result"]:
                for key in rtt:
                    if key == "x":
                        row.append(-1)
                    elif key == "rtt":
                        row.append(rtt[key])
                count += 1

            if count != r["sent"]:
                print("CAUTION: CHECK COUNTS!!")
            # for i in range(r["sent"] - count):
            #     row.append(-1)

            if "ttl" in r.keys():
                row.append(r["ttl"])

            row.extend([r["fw"], r["lts"],
                        r["dst_name"], r["af"],
                        r["dst_addr"], r["src_addr"],
                        r["proto"], r["size"], r["dup"], r["rcvd"], r["sent"], r["min"], r["max"],
                        r["avg"],
                        r["msm_id"], r["prb_id"], r["timestamp"], r["msm_name"], r["from"], r["type"],
                        r["group_id"],
                        r["step"], r["stored_timestamp"]])

            print(row)
            writer.writerow(row)

        # if "x" in r["result"][0].keys():
        #     print("in IF BLOCK")
        #     row = [r["result"][0], r["result"][1], r["result"][2], r["fw"], r["lts"], r["dst_name"], r["af"],
        #            r["dst_addr"], r["src_addr"],
        #            r["proto"], r["size"], r["dup"], r["rcvd"], r["sent"], r["min"], r["max"], r["avg"],
        #            r["msm_id"], r["prb_id"], r["timestamp"], r["msm_name"], r["from"], r["type"], r["group_id"],
        #            r["step"], r["stored_timestamp"]]
        # elif "error" in r["result"][0].keys():
        #     print("in ELIF BLOCK")
        #     print("Error: ", r["result"][0]["error"])
        #     row = [-2, -2, -2, r["fw"], r["lts"],
        #            r["dst_name"], r["af"],
        #            r["dst_addr"], r["src_addr"],
        #            r["proto"], r["size"], r["dup"], r["rcvd"], r["sent"], r["min"], r["max"],
        #            r["avg"],
        #            r["msm_id"], r["prb_id"], r["timestamp"], r["msm_name"], r["from"], r["type"],
        #            r["group_id"],
        #            r["step"], r["stored_timestamp"]]
        # else:
        #     print("in ELSE BLOCK")
        #     row = []
        #     count = 0
        #     for rtt in r["result"]:
        #         row.append(rtt)
        #         count += 1
        #
        #     for i in range(3 - count):
        #         row.append(-1)
        #
        #     row.append([r["fw"], r["lts"],
        #                 r["dst_name"], r["af"],
        #                 r["dst_addr"], r["src_addr"],
        #                 r["proto"], r["ttl"], r["size"], r["dup"], r["rcvd"], r["sent"], r["min"], r["max"],
        #                 r["avg"],
        #                 r["msm_id"], r["prb_id"], r["timestamp"], r["msm_name"], r["from"], r["type"],
        #                 r["group_id"],
        #                 r["step"], r["stored_timestamp"]])
