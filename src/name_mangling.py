# https://en.wikipedia.org/wiki/Name_mangling

class Yo(object):
    def __init__(self):
        self.__honey = True
        self.bro = True

assert Yo().bro
try:
    Yo().__honey
except AttributeError as e:
    print(f"{e}")
"""
In Python, the interpreter modifies (mangles) the class member
names starting with __ (double underscore a.k.a "dunder") and not ending with
more than one trailing underscore by adding _NameOfTheClass in front.
"""
assert Yo()._Yo__honey
assert "_Yo__honey" in Yo().__dict__

class Yo_second(object):
    def __init__(self):
        # Let's try something symmetrical this time
        self.__honey__ = True
        self.bro = True

assert Yo_second().bro
try:
  Yo_second()._Yo__honey__
except AttributeError as e:
  print(f"{e}")

assert "__honey__" in Yo_second().__dict__

_A__variable = "Some value"

class A(object):
    def some_func(self):
        return __variable # not initialized anywhere yet

# __variable is mangle to _A__variable
assert A().some_func() == "Some value"

try:
  A().__variable
except AttributeError as e:
  print(f"{e}")

assert "__variable" not in A().__dict__
