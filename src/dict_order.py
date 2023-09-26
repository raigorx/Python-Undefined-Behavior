from collections import OrderedDict

"""
Curly braces or the set() function can be used to create sets.
Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
"""
assert type({}) == dict
assert type(set()) == set


dictionary = dict()
dictionary[1] = "a"
dictionary[2] = "b"

ordered_dict = OrderedDict()
ordered_dict[1] = "a"
ordered_dict[2] = "b"

another_ordered_dict = OrderedDict()
another_ordered_dict[2] = "b"
another_ordered_dict[1] = "a"


class DictWithHash(dict):
    """
    A dict that also implements __hash__ magic.
    """

    __hash__ = lambda self: 0


class OrderedDictWithHash(OrderedDict):
    """
    An OrderedDict that also implements __hash__ magic.
    """

    __hash__ = lambda self: 0


assert dictionary == ordered_dict

assert dictionary == another_ordered_dict

"""
https://docs.python.org/3/library/collections.html#ordereddict-objects
Equality tests between OrderedDict objects are order-sensitive and are implemented as list(od1.items())==list(od2.items()).
Equality tests between OrderedDict objects and other Mapping objects are order-insensitive like regular dictionaries.
This allows OrderedDict objects to be substituted anywhere a regular dictionary is used.
"""
assert ordered_dict != another_ordered_dict

# {obj1, obj2, obj3} in python is a literal for set
assert type({"apple", "banana", "cherry"}) == set

try:
    len({dictionary, ordered_dict, another_ordered_dict})
except TypeError as e:
    print(f"dict don't have __hash__ implemented {e}")

dictionary = DictWithHash()
dictionary[1] = "a"
dictionary[2] = "b"

ordered_dict = OrderedDictWithHash()
ordered_dict[1] = "a"
ordered_dict[2] = "b"

another_ordered_dict = OrderedDictWithHash()
another_ordered_dict[2] = "b"
another_ordered_dict[1] = "a"

"""
because dictionary is equal to ordered_dict and another_ordered_dict
and its inserted first in the set, the set will contain only one object
however if dictionary is inserted last the two ordered_dict will be compared
and they are not equal so the set will contain two objects
"""
assert len({dictionary, ordered_dict, another_ordered_dict}) == 1
assert len({ordered_dict, another_ordered_dict, dictionary}) == 2

some_set = set()
some_set.add(dictionary)
assert ordered_dict in some_set

some_set.add(ordered_dict)
assert len(some_set) == 1

assert another_ordered_dict in some_set

some_set.add(another_ordered_dict)
assert len(some_set) == 1


another_set = set()
another_set.add(ordered_dict)
assert another_ordered_dict not in another_set

another_set.add(another_ordered_dict)
assert len(another_set) == 2

assert dictionary in another_set

another_set.add(another_ordered_dict)
assert len(another_set) == 2
