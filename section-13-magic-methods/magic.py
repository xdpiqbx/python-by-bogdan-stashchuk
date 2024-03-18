# print(bool)
# print(dir(bool))
# print(bool.__doc__)  # short documentation

my_list = []
print(f"id(my_list) is -> {id(my_list)}")
print(f"help(my_list.__eq__)\n{help(my_list.__eq__)}\n========")  # short method doc
print(help(my_list.__hash__))  # short method doc

print("-------- copy by link")
num1 = 10
print(id(num1))  # 1817352667664
num2 = num1
print(id(num2))  # 1817352667664

print(dir(__builtins__))
# [
#   'ArithmeticError', 'AssertionError', 'AttributeError',
#   'BaseException', 'BlockingIOError', 'BrokenPipeError',
#   'BufferError', 'BytesWarning', 'ChildProcessError',
#   'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
#   'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis',
#   'EncodingWarning', 'EnvironmentError', 'Exception', 'False',
#   'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
#   'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
#   'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
#   'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
#   'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
#   'NotADirectoryError', 'NotImplemented', 'NotImplementedError',
#   'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
#   'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
#   'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration',
#   'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
#   'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
#   'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning',
#   'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError',
#   '__build_class__', '__debug__', '__doc__', '__import__', '__loader__',
#   '__name__', '__package__', '__spec__',
#   'abs', 'aiter', 'all', 'anext', 'any', 'ascii',
#   'bin', 'bool', 'breakpoint', 'bytearray', 'bytes',
#   'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
#   'credits', 'delattr', 'dict', 'dir', 'divmod',
#   'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format',
#   'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex',
#   'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
#   'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
#   'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed',
#   'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
#   'super', 'tuple', 'type', 'vars', 'zip'
# ]

print(dir("some string"))

# [
#   '__add__', '__class__', '__contains__', '__delattr__',
#   '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#   '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
#   '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
#   '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
#   '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
#   '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#   'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
#   'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
#   'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
#   'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
#   'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
#   'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
#   'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
#   'swapcase', 'title', 'translate', 'upper', 'zfill'
#   ]
