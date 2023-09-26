"""
Python Subclass Relationships Aren't Transitive

Transitive is a term that often refers to a relationship where
if A relates to B and B relates to C
then A necessarily relates to C.
"""
from collections.abc import Hashable


a, b, c = 1, 2, 3

assert a < b
assert b < c
# Due to transitivity of '<', we can infer:
assert a < c


assert issubclass(list, object)

assert issubclass(object, Hashable)

assert issubclass(list, Hashable) is False
assert "__hash__" in dir(list)
assert getattr(list, "__hash__") is None


# A hashable class (by default)
class HashableClass:
    pass


assert "__hash__" in dir(HashableClass)
assert hasattr(HashableClass, "__hash__")


# A class that explicitly sets __hash__ to None, making it unhashable
class UnhashableClass:
    __hash__ = None


# A subclass that inherits from an unhashable class
class ChildOfUnhashable(UnhashableClass):
    pass


assert issubclass(HashableClass, Hashable)
assert issubclass(UnhashableClass, Hashable) is False
assert issubclass(ChildOfUnhashable, Hashable) is False
