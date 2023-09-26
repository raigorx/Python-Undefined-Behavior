def get_middle(some_list):
    mid_index = round(len(some_list) / 2)
    return some_list[mid_index - 1]


"""
get_middle([1]) only returned 1 because the index was round(0.5) - 1 = 0 - 1 = -1
returning the last element in the list.
"""
assert get_middle([1]) == 1
assert get_middle([1, 2, 3]) == 2
"""
This is not a float precision error, in fact, this behavior is intentional. Since Python 3.0, round() uses banker's rounding where .5 fractions are rounded to the nearest even number
This is the recommended way to round .5 fractions as described in IEEE 754. However,
the most popular programming languages (for example: JavaScript, Java, C/C++, Ruby, Rust) do not use banker's rounding either
"""
assert get_middle([1, 2, 3, 4, 5]) == 2
assert round(0.5) == 0
assert round(1.5) == 2
assert round(2.5) == 2
assert len([1, 2, 3, 4, 5]) / 2 == 2.5
assert round(len([1, 2, 3, 4, 5]) / 2) == 2
