"""
the __dict__ size in memory is implementation defined and can change between versions
here you can observer surprise behavior from the perpective of the programmer
test in 3.11.4 64 bits python windows
"""
import sys

class SomeClass:
    def __init__(self):
        self.some_attr1 = 1
        self.some_attr2 = 2
        self.some_attr3 = 3
        self.some_attr4 = 4


def dict_size(o):
    return sys.getsizeof(o.__dict__)

o1 = SomeClass()
o2 = SomeClass()
o1_size = dict_size(o1)
o2_size = dict_size(o2)
# normal expected behavior
assert o1_size == o2_size

del o1.some_attr1
o3 = SomeClass()
recalculate_o1_size = dict_size(o1)
# expected because an attribute was deleted
assert recalculate_o1_size != o1_size

o3_size = dict_size(o3)
# o1 was modified however is equal to o3
assert o3_size == recalculate_o1_size
# only o1 was modified however the 3 dicts are equal
assert dict_size(o3) == dict_size(o1) == dict_size(o2)

o1 = SomeClass()
o2 = SomeClass()
old_o1_size = dict_size(o1)
o1.some_attr5 = 5
o1.some_attr6 = 6
assert dict_size(o1) == old_o1_size
assert dict_size(o1) == dict_size(o2)
o3 = SomeClass()
assert dict_size(o3) == dict_size(o1) == dict_size(o2)