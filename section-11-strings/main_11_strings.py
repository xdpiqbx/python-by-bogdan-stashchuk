import os.path

the_string = "some string"
prog_langs = ["Python", "Java", "Go", "C++", "SQL"]
# print(type(the_string))  # <class 'str'>
# print(type(str))  # <class 'type'>
# print(dir(the_string))

# --------------------- Magic
#   '__add__', '__class__', '__contains__', '__delattr__',
#   '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#   '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
#   '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
#   '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
#   '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
#   '__setattr__', '__sizeof__', '__str__', '__subclasshook__'

# --------------------- Str
# print(the_string.capitalize())    # Some string
# print(the_string.lower())         # some string
# print(the_string.upper())         # SOME STRING
# print(the_string.title())         # Some String
# print("SoMe String".swapcase())   # sOmE sTRING
# print(the_string.casefold())      # Return the string for caseless comparisons

# print(the_string.count("s", 0, 6))  # there is 2 letters s in string

# print(the_string.encode())  # b'some string' (default encoding to utf-8)
# print(the_string.encode(encoding='UTF-8', errors='strict'))  # b'some string'

# --------------------- 'endswith', 'startswith'
# print(the_string.endswith("str", 1, 8))  # suffix can also be a tuple
# print(the_string.startswith("str", 5, 10))  # prefix can also be a tuple

# --------------------- 'expandtabs'
# print(the_string.expandtabs())  # tabs to spaces (default tab is 8 spaces)

# ---------- 'strip', 'lstrip', 'rstrip'
# print("|" + "    Hello    ".strip() + "    User...$$$".strip(" .$") + "|")  # |HelloUser|
# print("|" + "    Hello    ".lstrip() + "  . $ User    ".lstrip(" .$") + "|")  # |Hello    User    |
# print("|" + "    Hello    ".rstrip() + "    User    ".rstrip() + "|")  # |    Hello    User|

# ---------- 'find', 'rfind', 'index', 'rindex',
# print(the_string.find("s", 0, len(the_string)-2))  # 0 Return lowest index or -1 on failure.
# print(the_string.rfind("s", 0, len(the_string)-2))  # 5 Return highest index or -1 on failure.
# print(the_string.index("s", 0, len(the_string)-2))  # 0 Return lowest index or Raises ValueError if not found.
# print(the_string.rindex("s", 0, len(the_string)-2))  # 5 Return highest index or Raises ValueError if not found.

# ---------- 'center', 'ljust', 'rjust'
# print(the_string.center(20, "*"))  # ****some string*****
# print(the_string.ljust(20, "*"))  # some string*********
# print(the_string.rjust(20, "*"))  # *********some string

# ---------- 'zfill'
# If a string starts with '+' or '-', 0 digits are filled after the first sign prefix character.
# print("42".zfill(5))  # 00042
# print("-42".zfill(5))  # -0042
# print("+42".zfill(5))  # +0042
# print("text".zfill(8))  # 0000text
# print("-text".zfill(8))  # -000text
# print("+text".zfill(8))  # +000text

# ---------- 'removeprefix', 'removesuffix'
# some_url = "http://www.google.com"
# print(some_url.removeprefix("http://www."))  # google.com
# print(some_url.removesuffix(".com"))  # http://www.google

# ---------- 'replace'
# some_url = "http://www.google.com"
# print(some_url.replace("www.", ""))  # http://google.com
# print(some_url.replace(".com", ".net"))  # http://www.google.net
# print("aabcdefaaghaai".replace("a", "G", 3))  # GGbcdefGaghaai

# ---------- 'partition' & 'rpartition'
# print("abc|def|ghi|jkl|mno".partition("|"))  # ('abc', '|', 'def|ghi|jkl|mno')
# print("abc|def|ghi|jkl|mno".rpartition("|"))  # ('abc|def|ghi|jkl', '|', 'mno')

# ---------- 'join'
# separator = " -#- "
# print(separator.join(prog_langs))
# print(os.path.join("users", "Smith", "docs", "private"))

# ---------- 'split' & `rsplit`
# print("#".join(prog_langs).split("#", 2))  # ['Python', 'Java', 'Go#C++#SQL']
# print("#".join(prog_langs).rsplit("#", 2))  # ['Python#Java#Go', 'C++', 'SQL']

# ---------- 'splitlines'
# https://docs.python.org/3/library/stdtypes.html#str.splitlines

# result = """Lorem Ipsum is simply dummy text
# of the printing and typesetting industry.
# Lorem Ipsum has been the industry's
# standard dummy text ever since the 1500s,
# when an unknown printer took a galley
# of type and scrambled it to make a type specimen book.""".splitlines()

# print(result)  # every line of text is list element

# ['Lorem Ipsum is simply dummy text',
# 'of the printing and typesetting industry.',
# "Lorem Ipsum has been the industry's",
# 'standard dummy text ever since the 1500s,',
# 'when an unknown printer took a galley',
# 'of type and scrambled it to make a type specimen book.']

# ---------- 'maketrans' & 'translate'
# dict_table = str.maketrans("abc", "xyz", "sd")  # the first two maketrans arguments must have equal length
# dict_table = str.maketrans({"a": "cat", "b": "dog", "c": "snake"})  # string keys in translate table must be of length 1
# print("a b c b a".translate(dict_table))

# ---------- 'format'
# https://docs.python.org/3/library/stdtypes.html#str.format
# https://docs.python.org/3/library/string.html#format-examples
# print('Results of the {} {}'.format(2016, 'Referendum'))
# print('Results of the {0} {1}'.format(2016, 'Referendum'))
# print('Results of the {year} {event}'.format(year=2016, event='Referendum'))
# point = {'x': 4, 'y': -5}
# print('{x} {y}'.format(**point))

# ---------- 'format_map'
# https://docs.python.org/3/library/stdtypes.html#str.format_map
# point = {'x': 4, 'y': -5}
# print('{x} {y}'.format_map(point))

#   'isalpha',
#   'isascii',
#   'isidentifier',
#   'isalnum',
#   'isnumeric',
#   'isdigit',
#   'isdecimal',
#
#   'isprintable',
#   'isspace'
#   ,
#   'istitle',
#   'isupper'
#   'islower',
