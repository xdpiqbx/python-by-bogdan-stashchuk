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
int_num = 5
float_num = 4.5

print(True + int_num)  # 6
print(int_num + True)  # 6 -> int_num.__add__(True)
print(int_num + float_num)  # 9.5 "NotImplemented" but python do this -> float_num.__radd__(int_num)
print(float_num + int_num)  # 9.5 float_num.__add__(int_num)

# print(dir(__builtins__))
# https://docs.python.org/3/library/functions.html

# [
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

#   'GeneratorExit', 'SystemExit', 'exit',
#   'NotImplemented',
#   'StopAsyncIteration', 'StopIteration',
#   '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',

#   'str',
#   'int',
#   'float',
#   'bool',
#   'dict',
#   'list',
#   'set',
#   'frozenset',
#   'tuple',
#   'map',
#   'complex'  # complex(3, 5), complex('3+5j')

#   ord('*')  # 42
#   chr(42)  # function returns the character that represents the specified unicode
#   bin(42)  # function returns the binary version of a specified integer

#   abs(-42)  # Return the absolute value of a number

#   any(any_true_in_list)  # Check if any of the items in a list are True
#   all(all_true_list)  # Check if all items in a list are True

#   'getattr',
#   'setattr',
#   'hasattr',
#   'delattr',

#   'input',

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

#   'sum',
#   'divmod',
#   'max',
#   'min',
#   'pow',

#   'oct'  # The oct() returns an octal string from the given 'int' (binary, decimal or hexadecimal) number.
#   'hex'  # converts an 'int' to the hexadecimal number in string form

#   'breakpoint',
#   'bytearray',
#   'callable',
#   'classmethod',
#   'compile',
#   'copyright',
#   'credits',
#   'dir',
#   'enumerate',
#   'eval',
#   'exec',
#   'filter',
#   'format',
#   'globals',
#   'hash',
#   'help',
#   'id',
#   'isinstance',
#   'issubclass',
#   'len',
#   'license',
#   'locals',
#   'memoryview',
#   'object',
#   'open',
#   'print',
#   'property',
#   'quit',
#   'range',
#   'repr',
#   'reversed',
#   'round',
#   'slice',
#   'sorted',
#   'staticmethod',
#   'super',
#   'type',
#   'vars',
#   'zip'
# ]
