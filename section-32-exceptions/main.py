# ---------------------------------------- try except
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print(ZeroDivisionError)  # <class 'ZeroDivisionError'>
    print(type(error))  # <class 'ZeroDivisionError'>

    error.add_note("(Custom note) Error - Division by zero!")
    error.add_note("(Custom note) Some another note...")

    print(f"error -> {error}")  # division by zero
    print(f"error.__notes__ -> {error.__notes__}")
    print(f"error.args -> {error.args}")

    # print(dir(error))

print("Continue...\n")

# ---------------------------------------- try except except
try:
    print('10' / 0)
except ZeroDivisionError as error:
    print(f"error -> {error}")  # division by zero
except TypeError as error:
    # unsupported operand type(s) for /: 'str' and 'int'
    print(f"error -> {error}")

print("Continue...\n")

# ---------------------------------------- try except except else finally
try:
    print(0 / 10)
except ZeroDivisionError as error:
    print(f"error -> {error}")  # division by zero
except TypeError as error:
    # unsupported operand type(s) for /: 'str' and 'int'
    print(f"error -> {error}")
else:
    print("There was no error")
finally:
    print("Continue...\n")

# ---------------------------------------- If you do not know what happen
try:
    print(10 / 0)
except Exception as error:
    print(type(error))  # <class 'ZeroDivisionError'>
    print(isinstance(error, object))  # True
    print(isinstance(error, BaseException))  # True
    print(isinstance(error, Exception))  # True
    print(isinstance(error, ArithmeticError))  # True
    print(isinstance(error, ZeroDivisionError))  # True
    print(isinstance(error, TypeError))  # False

# --- never do this shit
try:
    print(10 / 0)
except:
    print("Some error error\n")

# Log services
# Logstash, Kibana

# ---------------------------------------- Custom exception


def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second arg can't be zero.")
    return a / b


try:
    divide_nums(10, 0)
except ValueError as error:
    print(error)
finally:
    print("Continue...\n")

# ---------------------------------------- Task

image_dict = {
    'image_id': 204,
    'image_title': 'kitty'
}


def image_info(image_data: dict) -> str:
    # if not image_data.get("image_id") or not image_data.get("image_title"):
    if "image_id" not in image_data or "image_title" not in image_data:
        error_message = "Not enough keys"
        error_message += ", ['image_id'] not exists" if not image_data.get(
            "image_id") else ""
        error_message += ", ['image_title'] not exists" if not image_data.get(
            "image_title") else ""
        raise KeyError(error_message)
    return f"Image {image_data['image_title']} has id {image_data['image_id']}"


try:
    print(image_info(image_dict))
except KeyError as error:
    print(error)
finally:
    print("Continue...")
