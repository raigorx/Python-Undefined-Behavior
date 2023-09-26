def some_func():
    assert Ellipsis

some_func()

assert ... is Ellipsis

"""
Ellipsis can be use as pass
"""
def yet_to_be_implemented_function():
    ...
"""
type-hint as reminder type hint are suggestion not enforcement
on this example its specified that the tuple can be any length
with float values
"""
from typing import Tuple
VectorND = Tuple[float, ...]  # any number of float values or integer or wathever
v1: VectorND = (1.0, 2.0)
v2: VectorND = (0, 5, "hello")
v3: VectorND = (1.0,)


"""
ellipsis can be use as sentinel value too
"""
def process_data(data, preprocess=None):
    if preprocess is Ellipsis:
        # Do some default preprocessing
        print("Default preprocessing!")