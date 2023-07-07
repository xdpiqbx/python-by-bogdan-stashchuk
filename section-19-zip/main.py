fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]
availability = [True, False, True]

zipped1 = list(zip(fruits, quantities, availability))
zipped2 = tuple(zip(fruits, quantities, availability))
zipped3 = set(zip(fruits, quantities, availability))
zipped4 = dict(zip(fruits, list(zip(quantities, availability))))

zipped1  # [('apple', 100, True), ('banana', 70, False), ('lime', 50, True)]
zipped2  # (('apple', 100, True), ('banana', 70, False), ('lime', 50, True))
zipped3  # {('lime', 50, True), ('apple', 100, True), ('banana', 70, False)}
zipped4  # {'apple': (100, True), 'banana': (70, False), 'lime': (50, True)}
