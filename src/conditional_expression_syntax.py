"""
reminder: ternary operator also called conditional expression
value_if_the_condition_is_true if condition_to_evaluate else value_if_the_condition_is_false
"""
x, y = (0, 1) if True else None, None
# expected x,y == (0, 1)
assert x == (0, 1)
assert y is None
assert (x, y) == ((0, 1), None)
"""
this is what happended first tuple is assigned to x, then y is assigned to None
"""
x = (0, 2) if True else None
assert x == (0, 2)

# if you want the expected result you have to do
x, y = (0, 1) if True else (None, None)
assert (x, y) == (0, 1)
