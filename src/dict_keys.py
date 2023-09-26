"""
python does implicit type conversion
so 5 becomes 5.0 and 5.0 becomes 5 + 0j
"""
assert 5 == 5.0 == 5 + 0j

"""
https://docs.python.org/3/library/functions.html#hash
Return the hash value of the object (if it has one). Hash values are integers.
They are used to quickly compare dictionary keys during a dictionary lookup.
Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
"""
assert hash(5) == hash(5.0) == hash(5 + 0j)

"""
of course those are not the same object
"""
assert 5 is not 5.0 is not 5 + 0j


some_dict = {}
some_dict[5.5] = "JavaScript"
some_dict[5.0] = "Ruby"
some_dict[5] = "Python"

assert some_dict[5.5] == "JavaScript"
assert some_dict[5.0] == "Python"
assert some_dict[5] == "Python"

complex_five = 5 + 0j
assert type(complex_five) == complex
assert some_dict[complex_five] == "Python"

some_dict = {}
some_dict[5] = "Ruby"
assert (5.0 in some_dict) and (5 + 0j in some_dict)
assert str(some_dict) == "{5: 'Ruby'}"

some_dict[5.0] = "JavaScript"
assert str(some_dict) == "{5: 'JavaScript'}"

del some_dict[5.0]
some_dict[5.0] = "C++"
assert str(some_dict) == "{5.0: 'C++'}"
