"""
{5: ({...}, 5)}
the ... means circular reference in other words
{...} is {5: (, 5)}
"""
a, b = a[b] = {}, 5
assert a == {5: (a, 5)}
assert a[5][0] is a
assert a[5][0] == {5: (a, 5)}

"""
same as above but in multiple lines for simpler understanding
"""
a, b = {}, 5
a[5] = a, 5
assert a == {5: (a, 5)}
assert a[5][0] is a

"""
similar to above but instead of using the same single dict(a) its using
two different dicts, so no circular reference
"""
a, b = {}, 5
a[b] = {}, 5
assert a == {5: ({}, 5)}

a = []
b = [a]
a.append(b)
# RecursionError: maximum recursion depth exceeded in comparison
# assert a[0][0][0][0] == [[[a]]]

"""
more examples of circular reference
"""
some_list = some_list[0] = [0]
assert some_list == [[some_list]]
assert some_list[0] == [[some_list]]
assert some_list is some_list[0]
assert some_list[0][0][0][0][0][0] == some_list
assert some_list[0][0][0][0][0][0] is some_list
