import sys

del_count = 0


class SomeClass:
    def __del__(self):
        global del_count
        del_count += 1
        print("deleted", self)


x = SomeClass()
y = x
# This will be 3, because:
# 2 for x and y,
# plus 1 for being an argument to getrefcount
assert sys.getrefcount(x) - 1 == 2
del x
assert sys.getrefcount(y) - 1 == 1
assert del_count == 0
del y
assert del_count == 1


x = SomeClass()
y = x
del x
assert del_count == 1
# assert "y" in globals()
del y
assert del_count == 2
print(globals())

"""
if you put the script below into the python interpreter line by line
you will see a different result, because the momement you type "y"
to see its value a reference to is is created an store to the magic variable _
so when you do "del y"
a reference to y still exist in the magic variable, but when you execute an expression
like globals() the magic variable _ is updated an now "y" no longer has reference
triggering the __del__ method
"""
"""
import sys
del_count = 0


class SomeClass:
    def __del__(self):
        global del_count
        del_count += 1
        print("deleted", self)

x = SomeClass()
y = x
# This will be 3, because:
# 2 for x and y,
# plus 1 for being an argument to getrefcount
assert sys.getrefcount(x) - 1 == 2
del x
y
assert sys.getrefcount(y) - 1 == 2
assert del_count == 0
del y
assert del_count == 0
globals()
assert del_count == 1
"""
