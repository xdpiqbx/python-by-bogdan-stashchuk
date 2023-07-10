import json

json_str = '{"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'

sneakers_dict = json.loads(json_str)
print("sneakers_dict => ", sneakers_dict)

sneakers_json_str = json.dumps(sneakers_dict, indent=2)
print("sneakers_json_str => ", sneakers_json_str)

# print(dir(json))
# ['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__',
#  '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#  '__package__', '__path__', '__spec__', '__version__', '_default_decoder',
#  '_default_encoder', 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps',
#  'encoder', 'load', 'loads', 'scanner']
