def get_variable_name(variable):
    return [name for name, value in globals().items() if value is variable][0]


# packing
packed = 1, 2, 3, 4
isinstance(packed, tuple) and print(f"{get_variable_name(packed)} is a tuple!")

# Unpacking the tuple into variables
one, two, three, four = packed
assert one == packed[0]
assert two == packed[1]
assert three == packed[2]
assert four == packed[3]

# Extended Unpacking
first, *middle, last = packed
assert first == packed[0]
assert middle == list(packed[1:-1])
assert last == packed[-1]
