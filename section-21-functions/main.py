#  https://www.udemy.com/course/python-ru/learn/lecture/35368642#overview
def empty():
    pass


def hello():
    print("Hello")


# print(type(hello))  # <class 'function'>

# print(dir(hello))
# --------------------------- Magic
# __annotations__
# __builtins__
# __call__
# __class__
# __closure__
# __code__
# __defaults__
# __delattr__
# __dict__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __get__
# __getattribute__
# __getstate__
# __globals__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __kwdefaults__
# __le__
# __lt__
# __module__
# __name__
# __ne__
# __new__
# __qualname__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__

# ---------------------------------- Task
def merge_lists_to_dict(lst_1: list, lst_2: list) -> dict:
    return dict(zip(lst_1, lst_2))


print(merge_lists_to_dict("abc", [1, 2, 3]))
