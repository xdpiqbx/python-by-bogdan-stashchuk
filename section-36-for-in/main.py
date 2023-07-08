# for in
# while

nums = [1, 2, 3, 4, 5, 6, 7, 8]
letters = ['a', 'b', 'c', 'd']
some_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

for i in nums:
    print(i)  # 1 2 3 4 5 6 7 8

for letter in letters:
    print(letter)  # a b c d

for key in some_dict:
    print(f"k={key}, v={some_dict[key]}")  # k=1, v=a k=2, v=b ...

for k, v in some_dict.items():
    print(f"k={k}, v={v}")

# --------------------------------- Task


def dict_to_list(my_dict: dict) -> list:
    return [(k * 2 if isinstance(k, int) else k, v) for k, v in my_dict.items()]


print(dict_to_list(some_dict))
# --------------------------------- Task


def filter_list(lst: list, tp: any) -> list:
    # return [item for item in lst if isinstance(item, tp)] # misses bool
    return [item for item in lst if type(item) is tp]


print(filter_list([1, False, 2, [1, 2, 3], 3, 4], int))

# --------------------------------- Task


def filter_list_1(lst: list, tp: any) -> list:
    return list(filter(lambda el: type(el) is tp, lst))


print(filter_list_1([1, False, 2, [1, 2, 3], 3, 4], int))
