"""
Scopes nested inside class definition ignore names bound at the class level.
generators expressions and list comprehensions have their own scope.
"""
import inspect

x = 5


class SomeClass:
    x = 17
    y = (x for i in range(10))
    z = [x for i in range(10)]

    def method():
        return x


generate_list = list(SomeClass.y)
assert generate_list == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
generate_list = list(SomeClass.z)
assert generate_list == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
assert SomeClass.method() == 5
