# In python we have:
# - Global scope
# - Function scope

# -------------------------- docstring
def my_func(name):
    """
    This function is good =)

    Args:
        name(str): any name
    """
    return f"Hello {name}"


my_func('Billy')


# -------------------------- global
a = 1


def for_global():
    global a
    a = 10


for_global()

print(a)  # if you have call for_global() -> 10 otherwise -> 1

print(dir())  # ... 'a', 'for_global', 'my_func'
