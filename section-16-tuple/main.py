# tuple is immutable
new_tuple = (1, 2, 3)
print(dir(tuple))
print(new_tuple)
print(new_tuple[0])
# del (new_tuple[0])  # 'tuple' object doesn't support item deletion
# new_tuple[0] = 4  # 'tuple' object does not support item assignment

# ---------------------- Methods
# .count()
# .index(serch, [find from index])

list_from_tuple = list(new_tuple)
list_from_tuple.append(4)
new_tuple = tuple(list_from_tuple)
print(new_tuple)

letters_tuple = tuple("abcd")
print(letters_tuple)  # ('a', 'b', 'c', 'd')
