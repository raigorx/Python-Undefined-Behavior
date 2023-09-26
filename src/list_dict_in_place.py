some_list = [1, 2, 3]
some_dict = {"key_1": 1, "key_2": 2, "key_3": 3}

some_list = some_list.append(4)
some_dict = some_dict.update({"key_4": 4})

"""
append and update modify the list and dict in place, and return None
"""
assert some_list is None
assert some_dict is None
