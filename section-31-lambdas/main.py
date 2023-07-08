# lambda params: expression

# ---------------------
def mult(a, b):
    return a * b

# same as


lambda a, b: a * b
# ---------------------
# ------ closure ------


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greet = greeting("Good, morning")
evening_greet = greeting("Good, evening")

print(morning_greet("Bill"))
print(evening_greet("Bill"))
