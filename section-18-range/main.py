# https://www.udemy.com/course/python-ru/learn/lecture/35368590#content

# range(start, stop, step)

my_range = range(1, 15, 2)
print(type(my_range))  # <class 'range'>
print(my_range)  # range(1, 15, 2)
print(list(my_range))  # [1, 3, 5, 7, 9, 11, 13]

print(my_range.index(5))  # 2
print(my_range.start)
print(my_range.stop)
print(my_range.step)

# print(dir(range))
# ------------------------ Methods
# .count(item) - 1 if el in range, otherwise 0
# .index(4) - to get item index in range
# start - readonly attribute
# stop - readonly attribute
# step - readonly attribute
