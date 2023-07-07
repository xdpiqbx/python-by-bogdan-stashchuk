set_nums = set()
set_fruits1 = set({"apple", "orange", "pear"})
set_fruits2 = {"orange", "apple"}
# print(set_fruits1 == set_fruits2)  # True/False

# ----- ERRORS! -----
# set_fruits1[0]  # 'set' object is not subscriptable
# del set_fruits1[0]  # 'set' object doesn't support item deletion
# lists_set = {[1, 2], [3, 4], [5, 6]}  # unhashable type: 'list', 'dict', 'set'

# print(dir(set))
# ----------------------------------- Methods
# add -> sme_set.add(any_item)
# union -> {1,2,3}.union({2,3,4}) -> {1, 2, 3, 4}
# union -> {1,2,3} | {2,3,4} -> {1, 2, 3, 4}
# pop -> remove and return random element from set
# copy -> copied_fruits = set_fruits1.copy()
# update -> like union
# remove -> set_fruits1.remove("apple") # remove el from set or KeyError
# discard -> set_fruits1.discard("apple") # remove el from set
# difference -> {1,2,3,4}.difference({1,2,3}) # {4}
# difference -> {1, 2, 3, 4} - {1, 2, 3} # {4}
# difference_update
# symmetric_difference -> {1,2,3}.symmetric_difference({1,2,4}) -> {3, 4}
# symmetric_difference -> (set_A | set_B) - (set_A & set_B) -> union differense intersection
# symmetric_difference_update
# intersection -> {1,2,3}.intersection({1,2,4}) # {1, 2}
# intersection -> {1,2,3} & {1,2,4} # {1, 2}
# intersection_update
# isdisjoint -> {1, 2, 3}.isdisjoint({4, 5, 6}) # True
# issubset -> {1, 2, 3}.issubset({1, 2, 3, 4}) # True
# issuperset -> {1, 2, 3, 4}.issuperset({1, 2, 3}) # True

# ----------------------------------- Task
a = {1, 2, 3, 4}
a.add(5)
b = {3, 4, 5, 6}
intersect_set = a.intersection(b)
print(list(intersect_set))
