# Dict unpack operator -> ' ** '

button = {
    'width': 200,
    'text': 'Buy',
    'color': 'blue'
}

red_button = {
    **button,
    'color': 'red',
    'opacity': 0.75
}

print(button)
print(red_button)

# ------------------------------

dict_1 = {1: "one"}
dict_2 = {2: "two"}

dict_3 = dict_1 | dict_2  # here dict_2 has more priority
# same as
dict_3 = {
    **dict_1,
    **dict_2,
}

print(dict_3)
