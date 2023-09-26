def some_func(default_arg=[]):
    default_arg.append("some_string")
    return default_arg


assert some_func() == ["some_string"]
assert some_func() == ["some_string", "some_string"]
"""
in the below code, we are passing an empty list, so the default argument becomes
the empty list, and the function appends the "some_string" to the empty list.

so yes the default argument persists across function calls
"""
assert some_func([]) == ["some_string"]
"""
here again we are not passing any argument, so the default argument is used
"""
assert some_func() == ["some_string", "some_string", "some_string"]


def some_func_new(default_arg=[]):
    default_arg.append("some_string")
    return default_arg


assert some_func_new.__defaults__ == ([],)
some_func_new()
assert some_func_new.__defaults__ == (["some_string"],)
some_func_new()
assert some_func_new.__defaults__ == (["some_string", "some_string"],)
assert some_func_new([]) == ["some_string"]
assert some_func_new.__defaults__ == (["some_string", "some_string"],)

"""
common fix for this behavior
"""


def some_func_fix(default_arg=None):
    if default_arg is None:
        default_arg = []
    default_arg.append("some_string")
    return default_arg
