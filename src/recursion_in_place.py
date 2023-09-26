result = []


def some_recursive_func(a):
    if a[0] == 0:
        return
    a[0] -= 1
    some_recursive_func(a)
    result.append(a)
    return a


"""
the recursion decrement a[0] until it reaches 0
and return it so [5, 0] becomes [0, 0]
the result return in every recursion is [0, 0]
because the operator -= modify the list in place
"""
assert some_recursive_func([5, 0]) == [0, 0]
assert result == [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

result = []


def similar_recursive_func(a):
    if a == 0:
        return a
    a -= 1
    similar_recursive_func(a)
    result.append(a)
    return a


"""
here the recursion decrement a until it reaches 0
but because integers are non-mutable the operator -= doesn't modify it in place
"""
assert similar_recursive_func(5) == 4
assert result == [0, 1, 2, 3, 4]
