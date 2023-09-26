class EXAMPLE:
    pass


"""
python compare objectt by identity not their content
Since EXAMPLE() creates a new instance each time it's called
these two instances are different objects with different memory addresses.
"""
assert EXAMPLE() != EXAMPLE()

"""
The is operator checks for object identity (i.e., if two references refer to the same object in memory).
"""
assert EXAMPLE() is not EXAMPLE()

"""
In Python, by default, the hash() of an object is derived from its id(), which is unique for distinct objects and ensures different memory addresses.
But there's a catch: the hash of short-lived objects (objects that are quickly created and destroyed, like in this case) can be reused.
"""
assert hash(EXAMPLE()) == hash(EXAMPLE())


class SAMPLE:
    def __init__(self):
        print(f"Constructor {id(self)}")

    def __del__(self):
        print(f"Destructor {id(self)}")


"""
The order of objeect creation and destruction is what makes the difference
between id and (is operator)
in id the object is created and destroyed before the call to id
but in (is operator) both objects are created the is operator is called
and after it the objects are destroyed.

And the last key point is that Cpython use the same memory address for the
newly created object if the previous object is destroyed.
"""
print("id == id")
assert id(SAMPLE()) == id(SAMPLE())
print("SAMPLE is SAMPLE")
assert SAMPLE() is not SAMPLE()
