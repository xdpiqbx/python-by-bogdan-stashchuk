# https://www.udemy.com/course/python-ru/learn/lecture/35368660#overview
def sum_num1(a, b):  # a, b -> required positional args
    return a + b

# ------------------- * - syntax
def sum_num2(a, *args, b):  # *args tulpe of args
    print(f"a={a}, args={args}, b={b}")
    return args[0] + args[1]


# sum_num2(1, 2, 3, b=4)

# Errors
# sum_num2(1, 2, 3, 4) TypeError: sum_num2() missing 1 required keyword-only argument: 'b'

# ------------------- Keyword args
def sum_num3(a, b):
    print(f"a={a} and b={b}")
    return b + a


# sum_num3(b=3, a=2)  # keyword arguments

# Errors
# sum_num3(b=3, 2) SyntaxError: positional argument follows keyword argument
# sum_num3(3, a=2) TypeError: sum_num3() got multiple values for argument 'a'
# -------------------

def sum_num4(z, x, *args, **kwargs):
    print(args)  # (7, 7, 7)
    print(kwargs)  # {'c': 3, 'b': 2, 'd': 4, 'a': 1}
    return kwargs.get('a') + kwargs.get('b')


print(sum_num4(98, 89, 7, 7, 7, c=3, b=2, d=4, a=1))

# Errors
# sum_num4(1, 2, 3, 4) TypeError: sum_num4() takes 0 positional arguments but 4 were given
# def sum_num4(z, x, **kwargs, y): ... [y] SyntaxError: arguments cannot follow var-keyword argument

# -------------------

# def any_func(positional, tuple_args, kw_args):...
