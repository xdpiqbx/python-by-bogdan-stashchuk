from copy import deepcopy

#  -------------------------- Immutable case
num_1 = 10
num_2 = 10

print(id(num_1))
print(id(num_2))
print(id(10))

print(id(num_1) == id(num_2) == id(10))

#  -------------------------- Mutable case
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_2  # it will bee same address (copy by link)
list_4 = list_3.copy()  # it will bee different address (shallow copy by values)
list_5 = deepcopy(list_3)  # it will copy all dicts, lists ... by they values

print(id(list_1))
print(id(list_2))
print(id(list_3))
print(id(list_4))
print(id(list_5))
print(id([1, 2, 3]))

# Every Mutable object have his own address.
# Except list_3 = list_2
