def name(n):
    print(n)


def fn_with_callback(data, callback_fn):
    callback_fn(data)


fn_with_callback("Billy", name)
