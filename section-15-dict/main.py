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

# print(dir(motorbike))
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
print(id(book))
print(book.items())  # dict_items([('title', 'Sword'), ('author', 'Bill')])
print(book.keys())  # dict_keys(['title', 'author'])
# print(book.popitem())  # ('author', 'Bill') was removed and returned
del (book["author"])

# ----------------------------- Convert
nums_list = [[1, "one"], [2, "two"], [3, "three"]]
nums_tuple = ([1, "one"], [2, "two"], [3, "three"])
nums_tuple_tuple = ((1, "one"), (2, "two"), (3, "three"))
nums_list_tuples = [(1, "one"), (2, "two"), (3, "three")]
nums_dict1 = dict(nums_list)  # {1: 'one', 2: 'two', 3: 'three'}
nums_dict2 = dict(nums_tuple)  # {1: 'one', 2: 'two', 3: 'three'}
nums_dict3 = dict(nums_tuple_tuple)  # {1: 'one', 2: 'two', 3: 'three'}
nums_dict4 = dict(nums_list_tuples)  # {1: 'one', 2: 'two', 3: 'three'}
print(nums_dict1)
print(nums_dict2)
print(nums_dict3)
print(nums_dict4)

# ----------------------------- Task
task_dict = dict()
key = input("input key")
val = input("input val")
task_dict[key] = val
key = input("input key")
val = input("input val")
task_dict[key] = val
key = input("input key")
val = input("input val")
task_dict[key] = val
print(task_dict)
