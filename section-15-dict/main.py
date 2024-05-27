#  https://www.udemy.com/course/python-ru/learn/lecture/35368548#overview

print(dict.__doc__)
# dict() -> new empty dictionary
# dict(mapping) -> new dictionary initialized from a mapping object's
#     (key, value) pairs
# dict(iterable) -> new dictionary initialized as if via:
#     d = {}
#     for k, v in iterable:
#         d[k] = v
# dict(**kwargs) -> new dictionary initialized with the name=value pairs
#     in the keyword argument list.  For example:  dict(one=1, two=2)

motorbike = {
    'brand': 'Ducati',
    'price': 10000,
    'engine_vol': 1.2,
    True: "Hello",
    3.14: "Some float kv",
    (1, 2): "Tuple val"
    # [1, 2, 3]: {1: "one"}  # unhashable type: 'list'
    # {1: 2}: "DictVal"  # unhashable type: 'dict'
}
car = dict()  # new empty dict
# # print(motorbike.__doc__)
# print(len(motorbike))  # keys count
# print(motorbike.get('engine_vol'))  # 1.2
# print(motorbike.get(1 == 1))  # Hello
# print(motorbike.get(1 > 1))  # None, because key not exists
# print(motorbike.get(1 > 1, "Default value"))  # Default value
# # print(motorbike[1 > 1])  # KeyError: False
# print(motorbike[(1, 2)])  # TupleVal
# print(motorbike[3.14])  # Some float kv

print(dir(motorbike))
# '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
# '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# ----------------------------- Methods
# .get(key, [default_val])
# items
# keys
# clear
# copy
# fromkeys
# pop
# popitem
# setdefault
# update
# values

# ----------------------------- Practice

book = dict()
book["title"] = "Sword"
book["author"] = "Bill"
book["is_new"] = True
print(id(book))
print(book.items())  # dict_items([('title', 'Sword'), ('author', 'Bill'), ('is_new', True)])
print(book.keys())  # dict_keys(['title', 'author', 'is_new'])
print(book.values())  # dict_values(['Sword', 'Bill', True])
print(book.fromkeys([1, 2, 3]))  # {1: None, 2: None, 3: None}
print(book.get("title", "Default value"))  # Sword / None if not exists or Default value
print(book.pop("is_new"))  # return+remove by key
print(book["title"])  # Sword
# print(book.popitem())  # ('author', 'Bill') was removed and returned
del (book["author"])

# ----------------------------- Copy
new_book = book.copy()
print(id(book))
print(id(new_book))
print(book)
print(new_book)

# ----------------------------- Convert
# nums_list = [[1, "one"], [2, "two"], [3, "three"]]
# nums_tuple = ([1, "one"], [2, "two"], [3, "three"])
# nums_tuple_tuple = ((1, "one"), (2, "two"), (3, "three"))
# nums_list_tuples = [(1, "one"), (2, "two"), (3, "three")]
# nums_dict1 = dict(nums_list)  # {1: 'one', 2: 'two', 3: 'three'}
# nums_dict2 = dict(nums_tuple)  # {1: 'one', 2: 'two', 3: 'three'}
# nums_dict3 = dict(nums_tuple_tuple)  # {1: 'one', 2: 'two', 3: 'three'}
# nums_dict4 = dict(nums_list_tuples)  # {1: 'one', 2: 'two', 3: 'three'}
# print(nums_dict1)
# print(nums_dict2)
# print(nums_dict3)
# print(nums_dict4)

# ----------------------------- Task
# task_dict = dict()
# key = input("input key")
# val = input("input val")
# task_dict[key] = val
# key = input("input key")
# val = input("input val")
# task_dict[key] = val
# key = input("input key")
# val = input("input val")
# task_dict[key] = val
# print(task_dict)
