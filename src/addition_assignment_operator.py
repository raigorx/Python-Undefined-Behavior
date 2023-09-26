"""
a = a + [5, 6, 7, 8]
is not the same as
a += [5, 6, 7, 8]

the assigment operator = create a new variable and assign it to the variable name
the += operator mutate the variable in place.
"""
a = [1, 2, 3, 4]
b = a
assert b is a
previous_a_id = id(a)
a = a + [5, 6, 7, 8]
assert id(b) == previous_a_id
assert b is not a
assert a == [1, 2, 3, 4, 5, 6, 7, 8]
assert b == [1, 2, 3, 4]

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7, 8]
assert a is b
assert a == [1, 2, 3, 4, 5, 6, 7, 8]
assert b == [1, 2, 3, 4, 5, 6, 7, 8]
