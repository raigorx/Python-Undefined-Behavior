import types


class CallableClass:
    def __call__(self):
        return 2 * 2


class SomeClass:
    def method(self):
        print(f"method called with self: {self}")
        # return 3**3

    @classmethod
    def class_method(cls):
        print(f"class_method called with self: {cls}")

    @staticmethod
    def static_method():
        pass


"""
In Python, a descriptor is an object attribute with "binding behavior",
one whose attribute access has been overridden by methods in the descriptor protocol.
These methods are __get__(), __set__(), and __delete__().
If an object defines any of these methods, it's considered a descriptor.

let's manually invoke the descriptor mechanism:
"""
bound_func = SomeClass.method.__get__(CallableClass)
"""
bound_func is a bound method object
"""
assert isinstance(bound_func, types.MethodType)
"""
the parameter pass to __get__ is the self that receives the method call
"""
assert getattr(bound_func, "__self__") == CallableClass
bound_func()

"""
methods accessed through the class are not bound to an object
so no self is passed
"""
assert not hasattr(SomeClass.method, "__self__")

obj1 = SomeClass()
obj2 = SomeClass()

assert bound_func.__self__ != obj1.method.__self__
"""
obj1.method creates a new method object each time it is accessed
that makes it have a different identity(address)
obj1.method this create an object
obj1.method() this calls the object
"""
assert isinstance(obj1.method, types.MethodType)
assert obj1.method is not obj1.method

"""
However accessing the method through the class does not create a new object
that makes it have the same identity(address)
"""
assert not isinstance(SomeClass.method, types.MethodType)
assert SomeClass.method is SomeClass.method

"""
@classmethod creates a method object when accessed through the class too
that makes it have a different identity(address)

Class methods are descriptors that, when accessed,
create a method object which are passed as the first argument the class(cls)
instead of an instance(self)
"""
assert SomeClass.class_method is not SomeClass.class_method
assert SomeClass.class_method == SomeClass.class_method
assert hasattr(SomeClass.class_method, "__self__")
assert obj1.class_method is not obj1.class_method

"""
@staticmethod does not create a method object when accessed through the class
that makes it have the same identity(address)
"""
assert SomeClass.static_method is SomeClass.static_method
assert obj1.static_method is obj1.static_method
assert (
    obj1.static_method
    is obj1.static_method
    is obj2.static_method
    is SomeClass.static_method
)

"""
the == operator checks value equality. For the bound method objects,
their __eq__ method is implemented to check if the method's function (__func__) and the bound object (__self__) are equal.

so obj1 and obj2 have same (__func__) but different (__self__)
"""
assert obj1.method != obj2.method

"""
obj1 and obj2 have same (__func__) and same (cls)
same for SomeClass.class_method
"""
assert obj1.method == obj1.method
assert obj1.class_method == obj1.class_method
assert obj1.class_method == obj2.class_method

"""
the above assertions as one
"""
assert (
    obj1.class_method
    == obj1.class_method
    == obj2.class_method
    == SomeClass.class_method
)
