import math
import random  # PSEUDO !!!
import secrets
import string

# ======================================================================== import random

print(random.random())  # rand num from 0 to 1 like -> 0.885349070081732

print(random.randint(1, 10))  # rand int from 1 to 10

print(random.choice([1, 2, 3, 4, 5]))  # rand from sequence
print(random.choice('abcdef'))  # rand char from sequence
print(random.choice(range(10)))  # rand char from range

print(random.choices([1, 2, 3, 4, 5, 6, 7, 8], k=3))  # [4, 7, 8]
print(''.join(random.choices('1234567890', k=8)))  # rand 8 digit PIN

lst = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lst)
print(lst)  # [5, 4, 2, 8, 3, 1, 6, 7]

# ======================================================================== import secrets, string
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.digits)  # 0123456789

all_chars = string.ascii_letters + string.digits + string.punctuation

print(secrets.choice(all_chars))  # random element
print(''.join(secrets.choice(all_chars) for char in range(8)))  # random sequence

# ======================================================================== import math

print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
print(math.sqrt(25))  # 5.0
print(math.log(100))  # 4.605170185988092
print(math.factorial(5))  # 120


# print(dir(math))  # 120
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__',
# 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh',
# 'ceil', 'comb', 'copysign', 'cos', 'cosh',
# 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1',
# 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
# 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt',
# 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter',
# 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt',
# 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# ======================================================================== recursion
def calc_factorial(num):
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num


print(calc_factorial(5))
