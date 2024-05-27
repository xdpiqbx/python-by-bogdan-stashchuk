# https://www.udemy.com/course/python-ru/learn/lecture/35368582#content

set_nums = set()
set_fruits1 = set({"apple", "orange", "pear"})
set_fruits2 = {"orange", "apple"}

# set_fruits1[0]  # TypeError: 'set' object is not subscriptable
# cars = {['type', 'Moto'], ['type', 'Car']}  # TypeError: unhashable type: 'list'
cars = {('type', 'Moto'), ('type', 'Car')}  # It's Ok!

# print(set_fruits1 == set_fruits2)  # True/False

print(type(set_fruits1))  # <class 'set'>
print(dir(set_fruits1))
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__',
# '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',
# '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__',
# '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__',
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update']

# ----- ERRORS! -----
# set_fruits1[0]  # 'set' object is not subscriptable
# del set_fruits1[0]  # 'set' object doesn't support item deletion
# lists_set = {[1, 2], [3, 4], [5, 6]}  # unhashable type: 'list', 'dict', 'set'

# print(dir(set))
# ----------------------------------- Methods
# add -> sme_set.add(any_item)
# union -> {1,2,3}.union({2,3,4}) -> {1, 2, 3, 4}
# union -> {1,2,3} | {2,3,4} -> {1, 2, 3, 4}
# difference -> {1,2,3,4}.difference({1,2,3}) # {4}
# difference -> {1, 2, 3, 4} - {1, 2, 3} # {4}
# intersection -> {1,2,3}.intersection({1,2,4}) # {1, 2}
# intersection -> {1,2,3} & {1,2,4} # {1, 2}
# symmetric_difference -> {1,2,3}.symmetric_difference({1,2,4}) -> {3, 4}
# symmetric_difference -> (set_A | set_B) - (set_A & set_B) -> union differense intersection

# pop -> remove and return random element from set
# copy -> copied_fruits = set_fruits1.copy()
# update -> like union
# remove -> set_fruits1.remove("apple") # remove el from set or KeyError
# discard -> set_fruits1.discard("apple") # remove el from set
# difference_update
# symmetric_difference_update
# intersection_update
# isdisjoint -> {1, 2, 3}.isdisjoint({4, 5, 6}) # True
# issubset -> {1, 2, 3}.issubset({1, 2, 3, 4}) # True
# issuperset -> {1, 2, 3, 4}.issuperset({1, 2, 3}) # True

# ----------------------------------- Task
# a = {1, 2, 3, 4}
# a.add(5)
# b = {3, 4, 5, 6}
# intersect_set = a.intersection(b)
# print(list(intersect_set))
