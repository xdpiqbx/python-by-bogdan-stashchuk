fruits1 = ["apple", "banana", "lime"]
fruits2 = ["apple", "banana", "lime"]
# print(fruits1 == fruits2)  # True

ids = [1, 2, 3, 4, 5]

# -------------------------------------- Methods
# print(dir(list))
# .append('item')
# .pop([index]) remove+return element from end or by index
# .sort([reverse=True])
# .count(item)
# .insert(index, item)  # insert item before index
# .clear()
# .copy()
# .extend(other_iterable)  # receives list or strind as param
# .index()
# .remove()
# .reverse()

# -------------------------------------- Other opts
new_list = fruits1 + fruits2
len(new_list)
del fruits1[0]  # del item by index

# -------------------------------------- Copy list
# copied_list0 = fruits1  # Do not do this! Link copy
copied_list1 = fruits1[:]
copied_list2 = fruits1.copy()
copied_list3 = list(fruits1)

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
print(dir(list))

l1 = [1, 2]
l2 = [3, 4]

merge_1 = l1 + l2
print(merge_1)

merge_2 = l1.__add__(l2)
print(merge_2)
