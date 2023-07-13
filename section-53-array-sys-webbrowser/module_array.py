from array import array

my_int_arr = array('i', [1, 2, 3, 4, 5, 3])

print(type(my_int_arr))  # <class 'array.array'>

my_int_arr.append(9)

print(my_int_arr)

# for i in my_int_arr:
#     print(i)

# my_int_arr.append("Hello") # TypeError: 'str' object cannot be interpreted as an integer

print(my_int_arr.count(3))  # 2
print(my_int_arr.pop())  # remove and return last element - 9
print(len(my_int_arr))  # 6

# ==================================== Write array to file
with open('my_arr.bin', 'wb') as my_file:
    my_int_arr.tofile(my_file)

imported_array = array('i')

with open('my_arr.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 6)  # (file, quantity of elements)
    print(imported_array)

imported_array.reverse()  # reverse arr
print(imported_array)

print(dir(array))
# ['__add__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
# '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#
# 'append', 'buffer_info', 'byteswap', 'count', 'extend', 'frombytes', 'fromfile', 'fromlist', 'fromunicode',
# 'index', 'insert', 'itemsize', 'pop', 'remove', 'reverse',
# 'tobytes', 'tofile', 'tolist', 'tounicode', 'typecode']
