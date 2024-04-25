# print(dir(list))
# '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# fruits1 = ["apple", "banana", "lime"]
# fruits2 = ["apple", "banana", "lime"]
# print(fruits1 == fruits2)  # True

# ids = [1, 2, 3, 4, 5]

# print(ids.__getitem__(0))  # sane as -> ids[0]

# -------------------------------------- Methods
# .append('item')
# .pop([index]) remove+return element from end or by index
# .sort(*, [key=None, reverse=False])  # MUTABLE!!! and return NONE
    # ----------------- https://docs.python.org/uk/3/howto/sorting.html#sortinghowto
# .count(item)  # returns the number of elements with the specified value
# .insert(index, item)  # insert item before index
# .clear() # Muttable! Return None/. List will be empty - []
# .copy()
# .extend(other_iterable)  # receives list or strind as param
# .index()
# .remove()
# .reverse()

# -------------------------------------- Other opts
# new_list = fruits1 + fruits2
# len(new_list)
# del fruits1[0]  # del item by index

# -------------------------------------- Copy list
# copied_list0 = fruits1  # Do not do this! Link copy
# copied_list1 = fruits1[:]
# copied_list2 = fruits1.copy()
# copied_list3 = list(fruits1)

# -------------------------------------- Task 1
# task_list_1 = [1, 2, 3, 4, 5]
# # task_list_1.remove(task_list_1[2])
# task_list_1.pop(2)
# print(len(task_list_1))
# task_list_1.reverse()
# task_list_2 = [8, 9]
# task_list_1.extend(task_list_2)
# print(task_list_1)

# -------------------------------------- Task 2

# l1 = [1, 2]
# l2 = [3, 4]
#
# merge_1 = l1 + l2
# print(merge_1)
#
# merge_2 = l1.__add__(l2)
# print(merge_2)
