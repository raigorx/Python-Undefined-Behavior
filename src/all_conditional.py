"""
This a simple example of the all() function in python.
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
"""

assert all([True, True, True])

assert all([True, True, False]) is False

"""
empty iterable is True
This behavior aligns with a principle in mathematics, where an empty set
has one element, the empty set itself.
"""
assert all([])

"""
False because the passed list has one element, [], and in python, an empty list is falsy
"""
assert all([[]]) is False
assert bool([]) is False

"""
higher recursive variants are always True.
This is because the passed array's single element ([[...]]) is no longer empty,
and lists with values are truthy
"""
assert all([[[]]])
