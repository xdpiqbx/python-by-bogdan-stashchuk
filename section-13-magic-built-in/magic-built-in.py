# print(bool)
# print(dir(bool))
# print(bool.__doc__)  # short documentation

# my_list = []
# print(f"id(my_list) is -> {id(my_list)}")
# print(f"help(my_list.__eq__)\n{help(my_list.__eq__)}\n========")  # short method doc
# print(help(my_list.__hash__))  # short method doc
#
# print("-------- copy by link")
# num1 = 10
# print(id(num1))  # 1817352667664
# num2 = num1
# print(id(num2))  # 1817352667664

# print(5 + "5")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print("5" + 5)  # TypeError: can only concatenate str (not "int") to str

# int_num = 5
# float_num = 4.5

# print(True + int_num)  # 6
# print(int_num + True)  # 6 -> int_num.__add__(True)
# print(int_num + float_num)  # 9.5 "NotImplemented" but python do this -> float_num.__radd__(int_num)
# print(float_num + int_num)  # 9.5 float_num.__add__(int_num)

# print(dir(__builtins__))
# https://docs.python.org/3/library/functions.html

#   ------- Errors
#   'ArithmeticError', 'AssertionError', 'AttributeError', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
#   'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
#   'ConnectionResetError', 'EOFError', 'EnvironmentError', 'FileExistsError', 'FileNotFoundError',
#   'FloatingPointError', 'IOError', 'ImportError', 'IndentationError', 'IndexError', 'InterruptedError',
#   'LookupError', 'IsADirectoryError', 'KeyError', 'MemoryError', 'ModuleNotFoundError', 'NameError',
#   'NotADirectoryError', 'NotImplementedError', 'OSError', 'OverflowError', 'PermissionError',
#   'ProcessLookupError', 'RecursionError', 'ReferenceError', 'RuntimeError', 'SyntaxError', 'SystemError',
#   'TabError', 'TimeoutError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
#   'UnicodeError', 'UnicodeTranslateError', 'ValueError', 'WindowsError', 'ZeroDivisionError',
#   ------- Exception
#   'Exception', 'BaseException',
#   ------- Warning
#   'Warning', 'BytesWarning', 'DeprecationWarning', 'EncodingWarning', 'FutureWarning', 'ImportWarning',
#   'PendingDeprecationWarning', 'ResourceWarning', 'RuntimeWarning', 'SyntaxWarning', 'UnicodeWarning',
#   'UserWarning'

#   'KeyboardInterrupt', 'None', 'False', 'True',

#   'GeneratorExit', 'SystemExit',
#   'NotImplemented',
#   'StopAsyncIteration', 'StopIteration',
#   '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',

# -------- 'ascii',
#     print(ascii("Hello"))  # Hello
#     test_str = "G ë ê k s f ? r G ? e k s"
#     print(ascii(test_str))  # 'G \xeb \xea k s f ? r G ? e k s'
# Python ascii() on new line characters
#     test_str = '''Geeks
#     for
#     geeks'''
#     print(ascii(test_str))  # 'Geeks\nfor\ngeeks'
# Python ascii() on Set
#     print("ascii on set:", ascii({"Š", "E", "T"}))  # {'T', 'E', '\u0160'}
# Python ascii() on List
#     print("ascii on list:", ascii(["Ň", "ĕ", "Ŵ"]))  # ascii on list: ['\u0147', '\u0115', '\u0174']
# Python ascii() on Tuple
#     print("ascii on tuple:", ascii(("Ģ", "Õ", "Õ", "D")))  # ascii on tuple: ('\u0122', '\xd5', '\xd5', 'D')

# -------- 'Ellipsis'  # The same as the ellipsis literal “...”.
#   print(Ellipsis)  # Ellipsis
#   print(...)  # Ellipsis
#   - Python Ellipsis is a built-in singleton object with no methods.
#   - You can use the Python Ellipses object with the Ellipsis term or the Ellipsis literal (...).
#   - The Ellipsis also uses as a placeholder in place of the "pass" keyword.
#   - Python Ellipsis object is a unique value used primarily
#       in conjunction with extended slicing syntax for data types container which is user-defined.
#   - Ellipsis is primarily used with Numpy for slicing.

# ----- bytes
#     byte_string = bytes("Hello", encoding='utf-8', errors='strict')
#     print(byte_string)  # b'Hello'
#     print(bytes.decode(byte_string, encoding='utf-8', errors='strict'))   # Hello
#     https://docs.python.org/3/library/codecs.html#standard-encodings
#     https://docs.python.org/3/library/codecs.html#error-handlers

# ----- bytearray
#  It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
#  bytearray(source, encoding, error)
# - Example
# my_string = "Hello World"
# my_bytes = bytearray(my_string, "utf-8")
# print(chr(my_bytes[0]))  # H
# my_bytes[0] = ord('X')
# new_string = my_bytes.decode("utf-8")
# print(new_string)  # Xello World

# ----- 'memoryview' - allows Python code to access the internal data of an object's buffer without making a copy of it
# byte_array = bytearray('XYZ', 'utf-8')
# mv = memoryview(byte_array)
# print(mv[0])  # 88 (Y-89, Z-90)
# print(bytes(mv[0:1]))  # b'X'
# mv[2] = 74  # Change Z to J
# print(byte_array)  # bytearray(b'XYJ')
# bytes_mv = bytes(mv)  # memory view to bytes
# str_mv = str(mv)  # memory view to str

# ----- SERVICE functions
#   'dir',
#   'help',
#   'copyright',
#   'credits',
#   'license',

#   'type' return type of an object in Python

#   'str'  # (__str__) Used for creating user-friendly output and for displaying the object as a string
#   'int',
#   'float',
#   'bool',
#   'bool',
#   'dict',
#   'list',
#   'set',
#   'frozenset',
#   'tuple',
#   'map',
#   'complex'  # complex(3, 5), complex('3+5j')

#   'repr'  # (__repr__) Used for debugging and development purposes to get the complete information of an object

#   'id'  # returns a unique id (the object's memory address) for the specified object
#   'hash'  # returns an integer value for every object which is hashable (is used to quickly compare dictionary keys)

#   'range'  # range(start, stop, step)

#   ord('*')  # 42
#   chr(42)  # function returns the character that represents the specified unicode
#   bin(42)  # function returns the binary version of a specified integer

#   abs(-42)  # Return the absolute value of a number

#   any(any_true_in_list)  # Check if any of the items in a list are True
#   all(all_true_list)  # Check if all items in a list are True

#   'print' & 'input',

# ----- 'iter' - create an iterator object
# 'reversed' - returns a reversed iterator object
# 'next'
# vowels = ["a", "e", "i", "o", "u"]
# vowels_iter = iter(vowels)
# print(next(vowels_iter))  # a
# print(next(vowels_iter))  # e
# print(next(vowels_iter))  # i
# print(next(vowels_iter))  # o
# print(next(vowels_iter))  # u
# print(next(vowels_iter))  # Traceback (most recent call last): StopIteration

# ----- 'aiter' & 'anext',
# https://docs.python.org/3/glossary.html#term-asynchronous-iterator
# https://docs.python.org/3/glossary.html#term-asynchronous-iterable
# https://docs.python.org/3/reference/expressions.html#await
# https://docs.python.org/3/reference/compound_stmts.html#coroutines

# ----- Math buildins
# 'sum', 'divmod', 'max', 'min', 'pow', 'round',

#   'oct'  # The oct() returns an octal string from the given 'int' (binary, decimal or hexadecimal) number.
#   'hex'  # converts an 'int' to the hexadecimal number in string form

#   'object'  # create empty object

#   'getattr', 'setattr', 'hasattr', 'delattr'

#   'classmethod'  # class_name.method = classmethod(class_name.method); or with @classmethod
#   'staticmethod'  # Calc.add_numbers = staticmethod(Calc.add_numbers); or with @staticmethod
#   'property',  # property(fget, fset, fdel, doc)
#   'isinstance'  # returns True if the specified object is of the specified type - isinstance(object, type)
#   'issubclass'  # returns True if the specified object is a subclass of the specified object - issubclass(object, subclass)

#   'super'  # returns proxy-object (temporary superclass object) for inheritance in classes

#   'globals'  # returns a dictionary representing the current global symbol table
#   'locals'  # returns the dictionary of the current local symbol table
#   'vars'  # vars(some_obj) | vars() argument must have __dict__ attribute

# ----- 'callable'
#   True, if the object appears to be callable.
#   False, if the object is not callable.

# ----- 'breakpoint' for debugging in console

# ----- 'open'  # open(file, mode)
#     "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#     "a" - Append - Opens a file for appending, creates the file if it does not exist
#     "w" - Write - Opens a file for writing, creates the file if it does not exist
#     "x" - Create - Creates the specified file, returns an error if the file exist
#     "t" - Text - Default value. Text mode
#     "b" - Binary - Binary mode (e.g. images)
# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp
# https://www.w3schools.com/python/python_file_remove.asp

# ----- 'compile'
#  The code object returned by the compile() method can later be called
#  using methods like: exec() and eval() which will execute dynamically generated Python code.
#     f = open('main.py', 'r')
#     temp = f.read()
#     f.close()
#     code = compile(temp, 'main.py', 'exec')
#     # ... some logic
#     exec(code)

#   'eval'  # used to evaluate a single dynamically generated Python expression
#   'exec'  # used to execute dynamically generated Python code only for its side effects

# ----- 'enumerate'  # enumerate(iterable, start=0)
# Returns an iterator with index and element pairs from the original iterable
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# enum_letters = enumerate(letters)  # enumerate(letters, 10)
# print(next(enum_letters))  # (0, 'a')
# print(list(enum_letters))  # [(1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]

#   'len'  # len(some_list or string) function returns the number of items in an object.

# ----- 'quit' - should not be used in production code!
# This function should only be used in the interpreter
# It raises the SystemExit exception behind the scenes
# for i in range(10):
#     if i == 5:
#         print(quit)  # ---- Use quit() or Ctrl-Z plus Return to exit
#         quit()
#     print(i)

# ----- 'exit' - It is like a synonym for quit() to make Python more user-friendly
# This function should only be used in the interpreter
# for i in range(10):
#     if i == 5:
#         print(exit)  # ---- Use exit() or Ctrl-Z plus Return to exit
#         exit()
#     print(i)

# ----- sys.exit([arg])  # arg - int or string
# is considered as exit commands in python if good to be used in production code

# sys.exit() is preferred mostly because the exit() and quit() functions cannot be used in production code
# while os._exit() is for special cases only when the immediate exit is required

# # ----- 'sorted' immutable
# ----------------- https://docs.python.org/uk/3/howto/sorting.html#sortinghowto
# # sorted(iterable, [key=key], [reverse=reverse])
# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x)
#
# a = ("aa", "cccc", "bbb")
# # Make it ordered by len in reversed direction
# x = sorted(a, key=len, reverse=True)  # ['cccc', 'bbb', 'aa']
# print(x)
#
# # Sort the list by the number closest to 10:
# # -- 1
# # def myfunc(n):
# #     return abs(10 - n)
# # -- 2
# # closest_10 = lambda n : abs(10 - n)
# # -- 3
# a = (5, 3, 1, 11, 2, 12, 17)
# x = sorted(a, key=lambda n: abs(10 - n))
# print(x)

# ----- filter(function, iterable) - returns an iterator where the items are filtered through a function.
# ages = [5, 12, 17, 18, 24, 32]
# print(list(filter(lambda age: age >= 18, ages)))

# ----- slice(start, end, step) - returns a slice object
# Alternative for slice is - itertools.islice(iterable, start, stop[, step])
# letters = ("a", "b", "c", "d", "e", "f", "g", "h")
# # x = slice(1, 8, 3)  # ('b', 'e', 'h')
# sliced_letters = slice(1, len(letters), 3)  # ('b', 'e', 'h')
# print(letters[sliced_letters])

# ----- zip(iterator1, iterator2, iterator3 ...)
# letters = ("a", "b", "c")
# numbers = (1, 2, 3, 4, 5)
# zipped = list(zip(letters, numbers))
# print(list(zipped))  # [('a', 1), ('b', 2), ('c', 3)]
# ltrs, nums = zip(*zipped)
# print(ltrs)
# print(nums)

# 'format'
# https://docs.python.org/2/library/string.html#format-specification-mini-language
# https://docs.python.org/2/library/string.html#format-specification-mini-language
