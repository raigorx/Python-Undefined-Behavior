some_str = "wthpython"
some_list = ['w', 't', 'h', 'p', 'y', 't', 'h', 'o', 'n']
assert some_list is not some_list[:] # False expected because a new object is created.
assert some_str is some_str[:] # True because strings are immutable, so making a new object is of not much use.
