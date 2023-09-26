assert isinstance(3, int)
assert isinstance(type, object)
assert isinstance(object, type)


class A:
    pass


assert isinstance(A, A) is False
assert isinstance(type, type)
assert isinstance(object, object)

assert issubclass(int, object)
assert issubclass(type, object)
assert issubclass(object, type) is False

# 1. All classes are either direct or indirect subclasses of 'object'.
assert issubclass(int, object)
assert issubclass(float, object)
assert issubclass(list, object)
assert issubclass(dict, object)
assert issubclass(str, object)
assert issubclass(type, object)

assert not object.__bases__

# 2. For most classes, 'object' is at the end of their method resolution order (MRO).
assert int.mro()[-1] == object
assert float.mro()[-1] == object
assert list.mro()[-1] == object

# For 'type' and 'object', they have a special relationship.
# 'type' is an instance of itself and 'object' is an instance of 'type'.
# Their MROs reflect their unique relationship.
assert type.mro(type) == [type, object]
assert object.mro() == [object]
