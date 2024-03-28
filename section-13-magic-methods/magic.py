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
# print(chr(my_bytes[0]))
# my_bytes[0] = ord('X')
# new_string = my_bytes.decode("utf-8")
# print(new_string)

# ----- 'memoryview'
# byte_array = bytearray('XYZ', 'utf-8')
# mv = memoryview(byte_array)
# print(mv[0])
# print(bytes(mv[0:1]))
# mv[2] = 74  # Change Z to J
# print(byte_array)
# bytes_mv = bytes(mv)  # memory view to bytes
# str_mv = str(mv)  # memory view to str

#   'GeneratorExit', 'SystemExit',
#   'NotImplemented',
#   'StopAsyncIteration', 'StopIteration',
#   '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',

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

# ----- 'iter' & 'next',
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
#       It raises the SystemExit exception behind the scenes
# for i in range(10):
#     if i == 5:
#         print(quit)  # ---- quit
#         quit()
#     print(i)


# ----- 'exit' - should not be used in production code!
# for i in range(10):
#     if i == 5:
#         print(exit)  # ---- exit
#         exit()
#     print(i)

# ----- sys.exit([arg])  # arg - int or string
# is considered as exit commands in python if good to be used in production code

# ----- 'filter'  # filter(boolean_function | None, iterable)
# numbers = [1, 2, 3, 4, 5, 6, 7]
# even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers)
# even_numbers = list(even_numbers_iterator)
# print(even_numbers)

# ----- 'reversed'  # returns a reversed copy of iterator object
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(list(reversed(letters)))
# print(letters)

# ----- 'sorted'  # sorted(iterable, key=key, reverse=reverse)
#     iterable - Required. The sequence to sort, list, dictionary, tuple etc.
#     key - Optional. A Function to execute to decide the order. Default is None
#     reverse - Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
# letters = ("h", "b", "a", "c", "f", "d", "e", "g")
# sorted_letters = sorted(letters, reverse=True)
# print(sorted_letters)

# ----- 'zip'  # zip(iterator1, iterator2, iterator3 ...)
# returns a zip object, which is an iterator of tuples
# where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
#     a = ("John", "Charles", "Mike")
#     b = ("Jenny", "Christy", "Monica")
#     x = zip(a, b)  # (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

#   'format'
#   'slice'
