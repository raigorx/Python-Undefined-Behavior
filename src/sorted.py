"""
The sorted method always returns a list, and comparing lists and tuples always returns False in Python.
"""
assert [] != tuple()
x = 7, 8, 9
assert isinstance(x, tuple)
assert isinstance(x, list) is False
assert sorted(x) == [7, 8, 9]
assert sorted(x) != x
assert sorted(x) == sorted(x)

y = reversed(x)
assert hasattr(y, "__iter__")
assert hasattr(y, "__next__")
assert sorted(y) == [7, 8, 9]
assert sorted(y) == []
y = reversed(x)
assert sorted(y) != sorted(y)
