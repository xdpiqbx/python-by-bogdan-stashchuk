# import math
# print(math.pi)  # 3.141592653589793
# print(math.e)  # 2.718281828459045
# print(math.tau)  # 6.283185307179586
# print(math.nan)  # nan

# import math as m
# print(m.pi)  # 3.141592653589793

# from math import e, tau, pi, nan
# print(pi)  # 3.141592653589793
# print(e)  # 2.718281828459045
# print(tau)  # 6.283185307179586

# ------------------------------------ Custom module

# from calc import *
# from calc import mult_nums, sum_nums as sum

import calc

print(calc.mult_nums(5, 4))
print(calc.PI)

print(dir(calc))
var = ['PI', '__builtins__', '__cached__', '__doc__', '__file__',
       '__loader__', '__name__', '__package__', '__spec__',
       'dif_nums', 'div_mod_nums', 'div_nums', 'mult_nums', 'sum_nums']

# ------------------------------------ __main__, __name__
# calc.py calc
# calc.py False - because calc imported
print("module_array.py", __name__)  # module_array.py __main__
print("module_array.py", __name__ == '__main__')  # module_array.py True

# ------------------------------------ built-in modules
help('modules')
# Enter any module name to get more help.  Or, type "modules spam" to search
# for modules whose name or summary contain the string "spam".
help('csv')  # csv - CSV parsing and writing... and other doc info

# ------------------------------------ packages
# create folder
# create __init__.py in folder
# add to folder files with funcs [file1, file2]
# import folder.file1
# from folder.file2 import function
