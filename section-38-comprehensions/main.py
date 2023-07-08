# list comprehensions [expression for item in list if condition]
# set comprehensions  {expression for item in set if condition}
# dict comprehensions {k: v for k, v in dict.items() if condition}

# create GENERATOR -> (num * num for num in range(7))

# -------------------- Dict from list using -> enumerate
lst = ['a', 'b', 'c', 'd']
dct = {i: val for i, val in enumerate(lst)}
print(dct)  # {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

# -------------------- Tasks
frist_dict = {'a': 'one', 'b': 'two', 'c': 'three'}
second_dict = {k.upper(): v for k, v in frist_dict.items()}
print(second_dict)

first_list = ['aaa', 'bbbb', 'sw']
second_list = [item for item in first_list if len(item) > 3]
print(second_list)

# -------------------- Generators
squares = (num * num for num in range(7))
print(squares)  # <generator object <genexpr> at 0x00...>
# -------------------------------------------------------- You can use generator only 1 time!
# print(list(squares))  # [0, 1, 4, 9, 16, 25, 36]
# print(tuple(squares))  # (0, 1, 4, 9, 16, 25, 36)
for num in squares:
    print(num)
    if num > 5:
        break
print("Next generator...")
for num in squares:
    print(num)
