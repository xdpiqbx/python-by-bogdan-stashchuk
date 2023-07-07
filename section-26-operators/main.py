# not # and # or
s = 1
print(not not s)  # True

# is
# is not
a = []
b = a
c = []
print(a is b)  # True because they have same id
print(b is not c)  # True because id is different

# in
# not in
print(0 in [0, 2, 3])  # True
print(1 not in [0, 2, 3])  # True

five = 5
six = 6
print(six.__eq__(six))  # ==
print(five.__ne__(six))  # !=
print(six.__ge__(five))  # >=
print(six.__gt__(five))  # >
print(five.__lt__(six))  # <
print(five.__le__(six))  # <=

print(id(a))
print(hex(id(a)))
