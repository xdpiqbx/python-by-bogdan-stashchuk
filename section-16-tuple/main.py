# tuple is immutable
new_tuple = (1, 2, 3)
print(dir(tuple))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__',
# 'count', 'index']

# print(new_tuple)
# print(new_tuple[0])
# # del (new_tuple[0])  # 'tuple' object doesn't support item deletion
# # new_tuple[0] = 4  # 'tuple' object does not support item assignment
#
# # ---------------------- Methods
# # .count([item]) # returns the number of elements with the specified value
# # .index([item], [find from index])
#
# list_from_tuple = list(new_tuple)
# list_from_tuple.append(4)
# new_tuple = tuple(list_from_tuple)
# print(new_tuple)
#
# letters_tuple = tuple("abcd")
# print(letters_tuple)  # ('a', 'b', 'c', 'd')
