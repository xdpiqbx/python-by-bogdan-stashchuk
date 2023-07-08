# if condition:
#   code...
# elif condition:
#   code...
# else:
#   code...

def route_info(data: dict) -> str:
    if 'distance' not in data and ('speed' not in data or 'time' not in data):
        return "No distance info is available"
    res_distance = data.get('distance') if 'distance' in data else data.get(
        'speed') * data.get('time')
    return f"Distance to your destination is {res_distance}"


print(route_info({'distance': 10}))
print(route_info({'speed': 100, 'time': 2}))
print(route_info({'speed': 100}))
