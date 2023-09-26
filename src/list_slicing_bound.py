"""
List slicing with out of the bounds indices throws no errors
"""
some_list = [1, 2, 3, 4, 5]
assert some_list[111:] == []