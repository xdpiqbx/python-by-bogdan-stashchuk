def is_user_authenticated():
    return False

def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT authenticated")
    return wrapper

@check_user_auth
def do_sensitive_job():
    print("Res of some tasks")

try:
    do_sensitive_job()
except Exception as error:
    print(error)

# def validate_args(fn):
#     def wrapper(*args, **kwargs):
#         for arg in [*args, *kwargs.values()]:
#             if not isinstance(arg, int) and not isinstance(arg, float):
#                 raise ValueError(f"{arg} type is {type(arg)}\n",
#                                  "Must be int or float")
#         return fn(*args, **kwargs)
#
#     return wrapper
#
# @validate_args
# def sum_nums(a, b):
#     return a + b
#
# try:
#     print(sum_nums(7, 2))
#     print(sum_nums(10.5, 2.3))
#     print(sum_nums(10.5, b='2.3'))
# except ValueError as error:
#     print(error)

# =====================================================
# def log_function_call(fn):
#     def wrapper(*args, **kwargs):
#         print(f"Function name is: [{fn.__name__}]")
#         print(f"Function args: {args} and kwargs: {kwargs}")
#         result = fn(*args, **kwargs)
#         print(f"Function result is <{result}>")
#         return result
#     return wrapper
#
# @log_function_call
# def mult(a, b):
#     return a * b\

# @log_function_call
# def sum(a, b):
#     return a + b
#
# print(mult(5, 2))
# print(sum(5, 2))

# ====================================================
# def decorator_fn(fn):
#     def wrapper_fn(*args, **kwargs):
#         print("Executed before")
#         result = fn(*args, **kwargs)
#         print("Function result:", result)
#         print("Executed after")
#         return result
#     return wrapper_fn
#
# @decorator_fn
# def my_function(a, b):
#     print("In my function")
#     return a, b
#
# print(my_function(100, 50))

# ====================================================

# def decorator_fn(fn):
#     def wrapper_fn(a, b):
#         print("Executed before")
#         result = fn(a, b)
#         print("Executed after")
#         return result
#     return wrapper_fn
#
# @decorator_fn
# def my_function(a, b):
#     print("In my function")
#     return a, b
#
# print(my_function(100, 50))

# ===================================================
# def decorator_fn(fn):
#     def wrapper_fn(a, b):
#         result = fn(a, b)
#         return result
#     return wrapper_fn
#
# @decorator_fn
# def my_fn(a, b):
#     return a, b
#
# print(my_fn(100, 50))
