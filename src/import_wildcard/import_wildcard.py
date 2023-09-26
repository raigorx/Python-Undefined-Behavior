"""
It is often advisable to not use wildcard imports.
in wildcard imports, the names with a leading underscore don't get imported.
"""

from module_error import *
from module_fix import *

assert some_weird_name_func_() == "works!"
try:
    _another_weird_name_func()
except NameError:
    print("The function _another_weird_name_func is not defined.")

assert some_weird_name_func_fix() == "works!"
assert _another_weird_name_func_fix() == "works!"
