result = [{"x": "*"}, {"x": "*"}, {"error": "sendto failed: Network is unreachable"}]

print("error" in result)
is_error = False
for item in result:
    if "error" in item.keys():
        is_error = True

print(is_error)
