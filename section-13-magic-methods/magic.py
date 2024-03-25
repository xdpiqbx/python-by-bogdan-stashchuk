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

#   'bool',
#   'chr',

#   'abs',
#   'aiter',
#   'all',
#   'anext',
#   'any',
#   'bin',
#   'breakpoint',
#   'bytearray',
#   'callable',
#   'classmethod',
#   'compile',
#   'complex',
#   'copyright',
#   'credits',
#   'delattr',
#   'dict',
#   'dir',
#   'divmod',
#   'enumerate',
#   'eval',
#   'exec',
#   'filter',
#   'float',
#   'format',
#   'frozenset',
#   'getattr',
#   'globals',
#   'hasattr',
#   'hash',
#   'help',
#   'hex',
#   'id',
#   'input',
#   'int',
#   'isinstance',
#   'issubclass',
#   'iter',
#   'len',
#   'license',
#   'list',
#   'locals',
#   'map',
#   'max',
#   'memoryview',
#   'min',
#   'next',
#   'object',
#   'oct',
#   'open',
#   'ord',
#   'pow',
#   'print',
#   'property',
#   'quit',
#   'range',
#   'repr',
#   'reversed',
#   'round',
#   'set',
#   'setattr',
#   'slice',
#   'sorted',
#   'staticmethod',
#   'str',
#   'sum',
#   'super',
#   'tuple',
#   'type',
#   'vars',
#   'zip'
# ]
