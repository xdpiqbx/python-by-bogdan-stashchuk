print(type(123))  # <class 'int'>>
print(type(int))  # <class 'type'>
print(dir(123))
# '__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
# '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
# '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
# '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__',
# '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__',
# '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
# '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
# '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
# '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
# '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator',
# 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'

print(type(12.3))  # <class 'float'>>
print(type(int))  # <class 'type'>
print(dir(12.3))
# '__abs__', '__add__', '__bool__', '__ceil__', '__class__',
# '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
# '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
# '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__int__', '__le__',
# '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
# '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__',
# '__rmul__', '__round__', '__rpow__',
# '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__',
# '__sub__', '__subclasshook__', '__truediv__', '__trunc__',
# 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real'

# Complex
print(type(12.3j))  # <class 'complex'>>
print(type(int))  # <class 'type'>
print(dir(12.3j))
# Attention with multiplication!
# j^2 == -1
# (10 + 7j)(3 + 3j) = 30 + 30j + 21j - 21 = 9 + 51j
# '__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__mul__', '__ne__', '__neg__', '__new__',
# '__pos__', '__pow__', '__radd__', '__reduce__', '__reduce_ex__',
# '__repr__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__',
# '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__',
# 'conjugate', 'imag', 'real'