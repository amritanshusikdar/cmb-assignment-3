import requests
import json
# import csv

# filename = "data/combined_measurements_traceroute.csv"

measurement_ids = [67606207, 67606208, 67606209, 67606210, 67606211, 67606212, 67606213, 67606214, 67606215, 67606216, 
                   67606217, 67606218, 67606219, 67606220, 67606221, 67606223, 67606224, 67606225, 67606226, 67606227, 
                   67606228, 67606229, 67606230, 67606231, 67606232, 67606234, 67606235, 67606236, 67606237, 67606238, 
                   67606239, 67606240, 67606241, 67606242, 67606243, 67606244, 67606245, 67606246, 67606247, 67606248, 
                   67606249, 67606251, 67606252, 67606253, 67606254, 67606255, 67606256, 67606257, 67606258, 67606259, 
                   67606260, 67606261, 67606262, 67606263, 67606264, 67606265, 67606266, 67606267, 67606268, 67606269, 
                   67606270, 67606271, 67606272, 67606273, 67606274, 67606275, 67606276, 67606277, 67606279, 67606280, 
                   67606281, 67606282, 67606283, 67606284, 67606285, 67606286, 67606287, 67606288, 67606289, 67606290, 
                   67606291, 67606293, 67606294, 67606295, 67606296, 67606297, 67606298, 67606299, 67606301, 67606302, 
                   67606303, 67606304, 67606305, 67606306, 67606307, 67606308, 67606309, 67606310, 67606311, 67606312, 
                   67606313, 67606314, 67606315, 67606316, 67606317, 67606318, 67606319, 67606320, 67606321, 67606322, 
                   67606323, 67606324, 67606326, 67606327, 67606328, 67606329, 67606330, 67606331, 67606332, 67606333, 
                   67606334, 67606335, 67606336, 67606337, 67606338, 67606339, 67606340, 67606341, 67606342, 67606343, 
                   67606344, 67606345, 67606346, 67606347, 67606348, 67606349, 67606350, 67606352, 67606353, 67606354, 
                   67606355, 67606356, 67606357, 67606358, 67606360, 67606361, 67606362, 67606363, 67606364, 67606365, 
                   67606366, 67606367, 67606368, 67606369, 67606370, 67606371, 67606372, 67606373, 67606374, 67606375]


def get_results(measurement_id):
    return json.loads(requests.get(
        f"https://atlas.ripe.net/api/v2/measurements/{measurement_id}/results/?format=json").text)

for measurement in measurement_ids:
    result = get_results(measurement)
    with open(f"data/traceroute_measurement_results/measurement_{measurement}_result.json", "w") as f:
        json.dump(result, f, indent=4)

"""
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # header = ["rtt1", "rtt2", "rtt3", "ttl", "fw", "lts", "dst_name", "af", "dst_addr", "src_addr", "proto",
    #           "size", "dup",
    #           "rcvd", "sent", "min", "max", "avg", "msm_id", "prb_id", "timestamp", "msm_name", "from", "type",
    #           "group_id", "step", "stored_timestamp"]

    header = ["fw", "mver", "lts", "endtime", "dst_name", "dst_addr", "src_addr", "proto", "af", "size", "paris_id",
              "destination_ip_responded", "msm_id",
              "prb_id", "timestamp", "msm_name", "from", "type", "group_id", "stored_timestamp"]

    writer.writerow(header)

    for measurement in measurement_ids:
        result = get_results(measurement)
        for r in result:
            row = []

            is_error = False
            for item in result:
                if "error" in item.keys():
                    is_error = True
                    break
            if is_error:
                print("---------ERROR ENCOUNTERED--------")
                print(r["result"])
                print("----------------------------------")

                # row.extend([-2, -2, -2, -2, r["fw"], r["lts"],
                #             r["dst_name"], r["af"],
                #             r["dst_addr"], r["src_addr"],
                #             r["proto"], r["size"], r["dup"], r["rcvd"], r["sent"], r["min"], r["max"],
                #             r["avg"],
                #             r["msm_id"], r["prb_id"], r["timestamp"], r["msm_name"], r["from"], r["type"],
                #             r["group_id"],
                #             r["step"], r["stored_timestamp"]])
                row.extend([-2, -2, -2, -2, r["fw"], r["mver"],
                            r["lts"], r["endtime"],
                            r["dst_name"], r["dst_addr"],
                            r["src_addr"], r["proto"], r["af"], r["size"], r["paris_id"], r["destination_ip_responded"], 
                            r["msm_id"], r["prb_id"],
                            r["timestamp"], r["msm_name"], r["from"], r["type"], r["group_id"], r["stored_timestamp"]])
                writer.writerow(row)
                continue

            count = 0
            for rtt in r["result"]:
                for key in rtt:
                    if key == "x":
                        row.append(-1.0)
                    elif key == "hop":
                        row.append(rtt[key])
                count += 1

            if count != r["sent"]:
                print("CAUTION: CHECK COUNTS!!")
            for i in range(3 - count):
                row.append(-1.0)

            if "ttl" in r.keys():
                row.append(r["ttl"])
            else:
                row.append(-1)

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

"""

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
