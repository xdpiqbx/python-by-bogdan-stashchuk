from os import path  # func style
from pathlib import Path  # OOP style

print("path.abspath('.') =>>", path.abspath('.'))
print(type(path))  # <class 'module'>

print("Path('.').absolute() =>>", Path('.').absolute())
print(type(Path))  # <class 'type'>
